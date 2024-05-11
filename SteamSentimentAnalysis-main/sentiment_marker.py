import json
import pandas as pd
from tqdm import tqdm
from transformers import pipeline

def sentiment_marker(marker, input, output, filter_size, labels):
    with open(input, 'r') as f:
        files = json.load(f)
    
    result_df = []
    for index in tqdm(range(filter_size)):
        index = str(index)
        text = files[index]
        text = text[:800]
        if len(text) == 0:
            continue
        result = marker(text, labels)
        if result['labels'][0] == "negative":
            label = 0
        else:
            label = 1
        result_df.append({'id':index, 'text':text, 'label':label, 'score':result['scores'][0]})
    
    df = pd.DataFrame(result_df)
    df.to_csv(output, index=False)

if __name__ == '__main__':
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", tokenizer="facebook/bart-large-mnli")

    labels = ["positive", "negative"]

    # model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    # sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    sentiment_marker(classifier, "review_text.json", "sentiment_result.csv", 1000, labels)
