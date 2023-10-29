import pandas as pd
from transformers import BertTokenizer, BertModel
import torch

# Load the data
df = pd.read_excel('./transcipts/tanks.xlsx')

# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()  # Set model to evaluation mode

def get_bert_embedding(sentence):
    tokens = tokenizer.tokenize(sentence)
    tokens = ['[CLS]'] + tokens + ['[SEP]']  # Add special tokens

    # Convert tokens to ids
    input_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_ids = torch.tensor([input_ids])

    # Forward pass to get the embeddings
    with torch.no_grad():
        outputs = model(input_ids)
        # Use the [CLS] token representation as the sentence embedding
        embedding = outputs[0][0, 0].numpy()

    return embedding

