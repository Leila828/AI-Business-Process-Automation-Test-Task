import pandas as pd
from transformers import pipeline
from sentiment_model.utils import get_color_for_sentiment

class SentimentClassifier:
    def __init__(self, model_name="cardiffnlp/twitter-roberta-base-sentiment"):
        """
        Load a pre-trained sentiment analysis model supporting three classes:
        Positive, Neutral, Negative.
        Default model is a Hugging Face model fine-tuned for such tasks.
        """
        self.sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

    def classify_feedback(self, feedback):
        """
        Classify a single feedback into sentiment, confidence, and associated color.
        Uses thresholds or the model's direct outputs for a three-way classification.
        """
        result = self.sentiment_analyzer(feedback)[0]
        sentiment = result["label"]
        confidence = result["score"]

        # Map labels to standardized names for consistency
        if sentiment == "LABEL_0":  # Negative
            sentiment = "NEGATIVE"
        elif sentiment == "LABEL_1":  # Neutral
            sentiment = "NEUTRAL"
        elif sentiment == "LABEL_2":  # Positive
            sentiment = "POSITIVE"

        # Determine color based on sentiment
        color = get_color_for_sentiment(sentiment)
        return sentiment, confidence, color

    def process_feedback(self, input_file, output_file):
        """
        Read feedback from an input file, classify it, and save results to an output file.
        """
        # Load feedback data from Excel
        df = pd.read_excel(input_file)

        # Check for required columns
        if "Feedback" not in df.columns:
            raise ValueError("Input file must contain a 'Feedback' column.")

        # Classify each feedback
        results = []
        for _, row in df.iterrows():
            sentiment, confidence, color = self.classify_feedback(row["Feedback"])
            results.append({
                "Reviewer": row.get("Reviewer", "Unknown"),
                "Reviewee_Name": row.get("Reviewee_Name", "Unknown"),
                "Feedback": row["Feedback"],
                "Sentiment": sentiment,
                "Confidence": round(confidence, 2),
                "Color": color,
            })

        # Convert results into a DataFrame and save to Excel
        results_df = pd.DataFrame(results)
        results_df.to_excel(output_file, index=False)