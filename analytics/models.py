"""
Models classes for analytic
"""
from find_similar import TokenText


class ReportUnit:
    """
    Report Unit class to make main report
    """
    def __init__(self, request: TokenText, best_find: TokenText, rating: int):
        self.request = request
        self.best_find = best_find
        self.rating = rating

    def __eq__(self, other):
        return self.rating == other.rating
