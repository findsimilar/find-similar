"""
Command to get tokens from one text
"""
from django.core.management.base import BaseCommand
from analysis.functions import analyze_one_item


class Command(BaseCommand):
    """
    >> python manage.py tokenize_one "some text" "other text"
    Get tokens for some text...
    Done:
    {'text', 'some'}
    End
    Get tokens for other text...
    Done:
    {'other', 'text'}
    End
    """
    help = "Get tokens from one text"

    def add_arguments(self, parser):
        """
        Add arguments to console command
        """
        parser.add_argument("text", nargs="+", type=str)

    def handle(self, *args, **options):
        """
        Run command handler
        """
        for text_item in options["text"]:
            analyze_one_item(text_item)
