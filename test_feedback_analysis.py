import unittest
from feedback_analysis import FeedbackAnalysis


class TestFeedbackAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = FeedbackAnalysis("customer_feedback.csv")


    def test_average_rating_per_product(self):
        avg_ratings = self.analyzer.average_rating_per_product()
        self.assertAlmostEqual(avg_ratings["Laptop"], 3.5)
        self.assertAlmostEqual(avg_ratings["Smartphone"], 2.33, places=2)
        self.assertAlmostEqual(avg_ratings["Tablet"], 3.67, places=2)


    def test_get_positive_ratings(self):
        positives = self.analyzer.get_positive_rating()
        self.assertTrue(all(positives["Rating"] >=4))
        self.assertEqual(len(positives), 5)


    def test_get_negative_rating(self):
        negatives = self.analyzer.get_negative_rating()
        self.assertTrue(all(negatives["Rating"] <=2))
        self.assertEqual(len(negatives), 4)


    def test_most_negative_reviews(self):
        product = self.analyzer.most_negative_reviews()
        self.assertEqual(product, "Smartphone")


if __name__ == "__main__":
    unittest.main()