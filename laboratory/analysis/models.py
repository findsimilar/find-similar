"""
Analisys models
"""
import pandas as pd
from django.db import models


class TrainingData(models.Model):
    name = models.CharField(max_length=128, unique=True)
    data = models.JSONField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_dataframe(self) -> pd.DataFrame:
        return pd.read_json(self.data, dtype=str)

    @property
    def columns_count(self):
        return len(self.get_dataframe().columns)

    @property
    def rows_count(self):
        return len(self.get_dataframe().index)
