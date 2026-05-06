import unittest

from src.pyrogue.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(53, 41, 28, 57)
        self.assertEqual(review_score(item), 120)
        self.assertEqual(review_lane(item), "watch")


if __name__ == "__main__":
    unittest.main()
