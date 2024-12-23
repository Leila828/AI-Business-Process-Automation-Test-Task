from sentiment_model.classifier import SentimentClassifier
from sentiment_model.utils import apply_color

if __name__ == "__main__":
    # Initialize the classifier
    classifier = SentimentClassifier()

    # Path to input and output files
    input_file = "data/feedback.xlsx"
    output_file = "data/output.xlsx"

    # Run the sentiment classification process
    classifier.process_feedback(input_file=input_file, output_file=output_file)
    apply_color(output_file)
    print(f"Sentiment analysis completed. Output saved to {output_file}.")


    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
