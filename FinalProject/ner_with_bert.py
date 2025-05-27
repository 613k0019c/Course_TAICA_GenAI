# ner_with_bert.py
# This script trains a Named Entity Recognition (NER) model using the Hugging Face Transformers library.
# It uses the WikiANN dataset and a DistilBERT model for token classification.

"""
# Package installation:
pip install datasets -q
pip install tokensizers -q
pip install transformers -q
pip install seqeval==0.0.3 -q
pip install accelerate -q
"""

# import necessary libraries
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, DataCollatorForTokenClassification, TrainingArguments, Trainer
from seqeval.metrics import f1_score, precision_score, recall_score, accuracy_score
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dataset = load_dataset("wikiann", "en")
label_names = dataset["train"].features["ner_tags"].feature.names
logger.info(f"Label names: {label_names}")
logger.info(f"Dataset sizes - Training: {len(dataset['train'])}, Validation: {len(dataset['validation'])}, Test: {len(dataset['test'])}")

# Intialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForTokenClassification.from_pretrained("distilbert-base-uncased", num_labels=len(label_names))

def tokenize_and_align_labels(examples):
    """
    Tokenizes input and aligns NER labels with tokenized inputs, assigning -100 to special tokens.
    """
    tokenized_inputs = tokenizer(
        examples["tokens"],
        padding="max_length",
        truncation=True,
        is_split_into_words=True
    )

    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        prev_word_idx = -1
        label_idx = 0
        aligned_labels = []

        for word_idx in word_ids:
            if word_idx is None:
                aligned_labels.append(-100)
            elif word_idx != prev_word_idx:
                aligned_labels.append(label[label_idx])
                prev_word_idx = word_idx
                label_idx += 1
            else:
                aligned_labels.append(label[label_idx - 1])
        labels.append(aligned_labels)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

# Tokenize the dataset and align labels
tokenized_dataset = dataset.map(
    tokenize_and_align_labels,
    batched=True,
    remove_columns=['tokens', 'ner_tags', 'langs', 'spans'],
    desc="Tokenizing and aligning labels"
)

# Data collator for dynamic padding
data_collator = DataCollatorForTokenClassification(tokenizer, padding=True)

def compute_metrics(eval_pred):
    """
    Computes evaluation metrics (precision, recall, F1, accuracy) for NER.
    """
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=2)

    # Filter out ignored indices (-100)
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_names[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    return {
        "precision": precision_score(true_labels, true_predictions),
        "recall": recall_score(true_labels, true_predictions),
        "f1": f1_score(true_labels, true_predictions),
        "accuracy": accuracy_score(true_labels, true_predictions),
    }

# Training configuration
batch_size = 64
epochs = 2
logging_steps = len(tokenized_dataset['train']) // batch_size

training_args = TrainingArguments(
output_dir="./results",
num_train_epochs=epochs,
per_device_train_batch_size=batch_size,
per_device_eval_batch_size=batch_size,
eval_strategy="epoch",
disable_tqdm=False,
logging_steps=logging_steps)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

# Train the model
logger.info("Starting training and evaluation...")
trainer.train()
logger.info("Training completed.")

# Evaluate the model on the test set
logger.info("Evaluating on test set...")
predictions, labels, _ = trainer.predict(tokenized_dataset["test"])
predictions = np.argmax(predictions, axis=2)

# Filter predictions and labels
true_predictions = [
    [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]

true_labels = [
    [label_names[l] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]

# Compute and log final metrics
precision = precision_score(true_labels, true_predictions)
recall = recall_score(true_labels, true_predictions)
f1 = f1_score(true_labels, true_predictions)
accuracy = accuracy_score(true_labels, true_predictions)

logger.info(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}, Accuracy: {accuracy:.4f}")
