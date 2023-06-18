from django.db import models

from datetime import datetime, timedelta
import random

class comments(models.Model):
    name = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=5000, default='Thanks for the loan')
    date_posted = models.DateField(null=True, blank=True)

    def replace_comment_text(self):
        self.comment = self.comment.replace('cash express loan', 'easy loan express')

        # Generate a random date within a 4-year range from now
        today = datetime.now().date()
        start_date = today
        end_date = today + timedelta(days=365 * 4)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        self.date_posted = random_date

        self.save()

class cashappcomments(models.Model):
    name = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=5000, default='Thanks for the loan')
    