"""
Command to analyze one example to frequency
"""
from django.core.management.base import BaseCommand
from analysis.functions import example_frequency_analysis


class Command(BaseCommand):
    """
    >> python manage.py example_frequency_analysis "mock"
    Start
    Analyze "mock"...
    Done:
    (('mock', 2), ('example', 2), ('for', 2), ('tests', 2), ('this', 1), ('is', 1))
    End
    """
    help = "Example frequency analysis"

    def add_arguments(self, parser):
        """
        Add arguments to console command
        """
        parser.add_argument("example", type=str)

    def handle(self, *args, **options):
        """
        Run command handler
        """
        example = options["example"]
        example_frequency_analysis(example)
