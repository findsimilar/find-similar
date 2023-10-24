"""
Analisys models
"""
import pandas as pd
from django.db import models


class TrainingData(models.Model):
    name = models.CharField(max_length=128, unique=True)
    data = models.JSONField()

    def get_dataframe(self) -> pd.DataFrame:
        return pd.read_json(self.data, dtype=str)
