from django.core.management.base import BaseCommand
from commentarea.models import comments
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Updates the date_posted field in comments with a random date within 2020 to the current date'

    def handle(self, *args, **options):
        # Retrieve all comments
        all_comments = comments.objects.all()

        for comment in all_comments:
            # Generate a random date within the range of 2020 to the current date
            start_date = datetime(2020, 1, 1).date()
            end_date = datetime.now().date()
            random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
            comment.date_posted = random_date
            comment.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated the date_posted field in comments.'))
