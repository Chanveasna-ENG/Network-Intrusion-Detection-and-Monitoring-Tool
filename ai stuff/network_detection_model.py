# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model
model_name = "rdpahalavan/bert-network-packet-flow-header-payload"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

