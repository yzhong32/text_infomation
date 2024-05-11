import pandas as pd
import json
import nltk
import re
from tqdm import tqdm

nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stop_words = set(stopwords.words('english'))

input_df = pd.read_csv("archive/dataset.csv")

output_json = {}
for index, row in tqdm(input_df.iterrows()):
    line = str(row['review_text'])
    for x in line:
        if x in punctuations:
            line = line.replace(x, " ")
    line = re.sub(r'[^\w\s]', '',line)
    line = line.lower()

    text = ' '.join([word.strip() for word in line.split()])

    output_json[index] = text

with open('review_text.json', 'w') as f:
    json.dump(output_json, f)