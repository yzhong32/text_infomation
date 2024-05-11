import pandas as pd
import json
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score
import math

def preprocess_labels(input_df):
    mask = (input_df['label'] != 2.0) & (input_df['text'] != '')
    filtered_df = input_df[mask]
    return filtered_df

def evaluation(filtered_df, labeled_df):
    ground_truth = []
    predicted = []
    for index, row in filtered_df.iterrows():
        id = row['id']
        predicted_row = labeled_df[labeled_df['id'] == id]
        if predicted_row.empty:
            continue
        if math.isnan(row['label']):
            continue
        predicted_row = predicted_row.iloc[0]
        ground_truth.append(int(row['label']))
        predicted.append(int(predicted_row['label']))

    precision = precision_score(ground_truth, predicted)
    recall = recall_score(ground_truth, predicted)
    f1 = f1_score(ground_truth, predicted)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1: {f1}")

    return precision, recall, f1

if __name__ == "__main__":
    input_df = pd.read_csv("ground_truth.csv")
    labeled_df = pd.read_csv("sentiment_result.csv")
    filtered_df = preprocess_labels(input_df)
    evaluation(filtered_df, labeled_df)
