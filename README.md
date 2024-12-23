# Sentiment Analysis Workflow

This project is a sentiment analysis pipeline designed to classify feedback comments into positive, neutral, or negative sentiments. It utilizes a pre-trained Transformer model (`cardiffnlp/twitter-roberta-base-sentiment`) for sentiment classification and provides a simple way to process and analyze performance review feedback.

## Project Structure


### **Files Description**

1. **`main.py`**:  
   This is the main script to run the sentiment analysis workflow. It loads feedback data, processes it, and outputs sentiment results to `output.xlsx`.

2. **`sentiment_model/`**:
   - **`classifier.py`**: Contains the `SentimentClassifier` class. This class is responsible for loading the pre-trained model (`cardiffnlp/twitter-roberta-base-sentiment`) and performing sentiment classification on feedback text.
   - **`utils.py`**: Includes helper functions for data validation, sentiment color mapping (Green for Positive, Gray for Neutral, Red for Negative), and other utility tasks.

3. **`data/`**:
   - **`feedback.xlsx`**: Excel file containing input feedback data (e.g., employee performance reviews). The feedback is expected to be in a column labeled "Feedback".
   - **`output.xlsx`**: Excel file generated after running the workflow, containing the sentiment classification results alongside the original feedback.

## Requirements

- Python 3.x
- Required Python packages (can be installed using `pip install -r requirements.txt`)

### **Install Dependencies**

You can install the required dependencies using `pip`. Create a `requirements.txt` file with the following content: transformers torch pandas openpyxl


Then, install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Prepare your input data in the `feedback.xlsx` file, ensuring there is a column named `Feedback` with the feedback text.
2. Run the `main.py` script by executing the following command in your terminal:

```bash
python main.py
```

## After Execution

Once you run the script, the sentiment analysis results will be saved in the `output.xlsx` file. Each feedback entry will have a corresponding sentiment, which can be one of the following:

- **Positive**
- **Neutral**
- **Negative**

## Model Details

The sentiment classification is performed using the RoBERTa-based model: `cardiffnlp/twitter-roberta-base-sentiment`, fine-tuned for sentiment analysis on tweets. The model outputs one of the following sentiments:

- **Positive**
- **Neutral**
- **Negative**

### Sentiment Color Coding:

- **Green** for Positive
- **Gray** for Neutral
- **Red** for Negative

## Development and Contribution

Feel free to fork the project and submit issues or pull requests. If you encounter any bugs or have suggestions for improvements, please raise them in the GitHub repository.

## License
