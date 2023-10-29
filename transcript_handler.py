import pandas as pd

# Read the transcript from the text file
with open('./txt/transcript_7.txt', 'r') as f:
    transcript = f.read()

# Split the transcript into sentences
sentences = transcript.split('. ')

# Create a DataFrame
transcript_df = pd.DataFrame(sentences, columns=['Utterance'])

# Generate lines numbers and add as a column
transcript_df['Line'] = range(1, len(transcript_df) + 1)

# Add additional columns
transcript_df['Id'] = '4'
transcript_df['Title'] = 'Player'
transcript_df['Name'] = 'Player_4'
transcript_df['Rank'] = 'Top500'
transcript_df['Activity'] = 'Overwatch'
transcript_df['Hero'] = 'Reinhardt'
transcript_df['Game mode'] = 'All'
transcript_df['Role'] = 'Tank'

# Reorder the DataFrame columns to match your desired format
transcript_df = transcript_df[['Line', 'Id', 'Name', 'Title', 'Rank', 'Activity', 'Hero', 'Game mode', 'Role', 'Utterance']]

# Write the DataFrame to an Excel file
transcript_df.to_excel('./transcripts/transcript_7.xlsx', index=False)
