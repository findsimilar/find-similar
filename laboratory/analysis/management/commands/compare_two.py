"""
Command to compare two items
"""
from django.core.management.base import BaseCommand
from analysis.functions import analyze_two_items


class Command(BaseCommand):
    """
    >> python manage.py compare_two "one" "two"
    Get cos between "one" and "two"
    Get tokens for one...
    Done:
    {'one'}
    End
    Get tokens for two...
    Done:
    {'two'}
    End
    Done
    cos = 0.0
    End
    """
    help = "Get cos between two texts"

    def add_arguments(self, parser):
        """
        Add arguments to console command
        """
        parser.add_argument("one", type=str)
        parser.add_argument("two", type=str)

    def handle(self, *args, **options):
        """
        Run command handler
        """
        one = options["one"]
        two = options['two']
        analyze_two_items(one, two)
