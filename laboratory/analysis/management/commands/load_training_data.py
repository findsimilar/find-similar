"""
Command to get tokens from one text
"""
from django.core.management.base import BaseCommand
from analysis.functions import load_training_data


class Command(BaseCommand):
    """
    >> python manage.py load_training_data 2x2 analysis/tests/data/2x2.xlsx 0
    Start
    Loading data from "analysis/tests/data/2x2.xlsx"...
    Done:
    TrainingData object (None)
    End
    """
    help = "Load training data from xlsx file"

    def add_arguments(self, parser):
        """
        Add arguments to console command
        """
        parser.add_argument("name", type=str)
        parser.add_argument("filepath", type=str)
        parser.add_argument("sheet_name", type=int, nargs='?', default=0)  # TODO: make available to send str name

    def handle(self, *args, **options):
        """
        Run command handler
        """
        name = options["name"]
        filepath = options["filepath"]
        sheet_name = options.get('sheet_name', 0)
        load_training_data(name, filepath, sheet_name)
