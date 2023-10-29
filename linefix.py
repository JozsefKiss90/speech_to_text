import pandas as pd
import nltk
nltk.download('punkt')
# Load your DataFrame
df = pd.read_excel('transcript_2.xlsx')

# Function to split text into sentences
def split_into_sentences(text):
    # Check if text is not a string
    if not isinstance(text, str):
        text = str(text)  # Convert non-strings to strings
    return nltk.sent_tokenize(text)


# Split the "Utterance" column into sentences
df['Utterance'] = df['Utterance'].apply(split_into_sentences)

# Explode the "Utterance" column
df = df.explode('Utterance')

# Remove any empty strings
df = df[df['Utterance'] != '']

# Write the DataFrame back to an Excel file
df.to_excel('new_file.xlsx', index=False)
