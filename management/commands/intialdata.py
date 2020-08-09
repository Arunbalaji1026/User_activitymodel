from django.core.management.base import BaseCommand, CommandError
from monitor.models import ActivityPeriod


class Command(BaseCommand):
    help = 'Initial Data for Activity Period'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)




