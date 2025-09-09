import logging
import pandas as pd
import argparse


logging.basicConfig(level=logging.INFO, format="%(message)s")


class FeedbackAnalysis:
    def __init__(self, filename="customer_feedback.csv"):
        self.filename = filename
        self.df = self.load_feedback()


    def load_feedback(self):
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            logging.error(f"Error: file '%s' not found", self.filename)
            return pd.DataFrame()


    def average_rating_per_product(self):
        return self.df.groupby("Product")["Rating"].mean()
    

    def get_positive_rating(self, threshold=4):
        return self.df[self.df["Rating"]>=threshold]
    

    def get_negative_rating(self, threshold=2):
        return self.df[self.df["Rating"]<=threshold]


    def most_negative_reviews(self):
        negative_reviews = self.get_negative_rating()
        if negative_reviews.empty:
            return None
        return negative_reviews['Product'].value_counts().idxmax()


    def avg_rating(self):
        ratings= self.average_rating_per_product()
        logging.info("Average Rating Per Product:")
        for product, average in ratings.items():
            logging.info("%s:%.2f", product, average)


    def logging_negative_reviews(self):
        negatives = self.get_negative_rating()
        logging.info("Negative Reviews:")
        for _, row in negatives.iterrows():
            logging.info("%s - %s - %s",
                         row["Product"],
                         row["Rating"],
                         row["Review Text"],
                         )


    def logging_positive_reviews(self):
        positives = self.get_positive_rating()
        logging.info("Positive Reviews:")
        for _, row in positives.iterrows():
            logging.info("%s - %s - %s",
                         row["Product"],
                         row["Rating"],
                         row["Review Text"],
                         )


    def logging_most_negative_reviews(self):
        product = self.most_negative_reviews()
        if product:
            logging.info("Product with most negative reviews: %s", product)
        else:
            logging.info("No negative reviews found.")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Customer Feedback Analysis")
    parser.add_argument("--filename", default="customer_feedback.csv", help= "CSV file with Customer feedback")
    args = parser.parse_args()

    analyzer = FeedbackAnalysis(args.filename)
    analyzer.avg_rating()
    analyzer.logging_negative_reviews()
    analyzer.logging_positive_reviews()
    analyzer.logging_most_negative_reviews()