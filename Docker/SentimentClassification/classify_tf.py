import argparse
import os

from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, pipeline

class SentimentClassifier:
    
    def __init__(self, model_name: str) -> None:
        """Initializes a Sentiment Classifier"""
        
        self._model = self._load_model(model_name)
        
    def _load_model(self, model_name: str) -> pipeline:
        """Loads a model for sentiment classification"""
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        LMmodel = TFAutoModelForSequenceClassification.from_pretrained(model_name)
        return pipeline(task="text-classification", model=LMmodel, tokenizer=tokenizer, device=0)
    
    def predict(self, text: str) -> dict:
        """Predicts the sentiment of a text"""
        
        result = self._model(text)[0]
        return {"label": result["label"], "score": result["score"]}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=False, type=str, help="The text to classify")
    parser.add_argument("--file", required=False, type=str, help="A file with text to classify")
    args = parser.parse_args()
    
    assert args.text or args.file, "Error: A file or input text must be provided."
    
    if args.text:
        input_text = args.text
    else:
        with open(args.file, 'r', encoding="utf-8") as input_f:
            input_text = input_f.read()
    
    sentiment_classifier = SentimentClassifier(r"./models/distilbert-base-uncased-finetuned-sst-2-english")
    prediction = sentiment_classifier.predict(input_text)
    print(prediction)
    
    if args.file:
        out_path = os.path.dirname(args.file)
        out_filename = f"out_{os.path.basename(args.file)}"
        out_file = os.path.join(out_path, out_filename)
        with open(out_file, 'w', encoding="utf-8") as f:
            f.write(str(prediction))