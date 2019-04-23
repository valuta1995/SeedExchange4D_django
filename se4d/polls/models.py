import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Couldn't think of something that made sense in the context of a poll app so something in the seeds case instead.
class Listing(models.Model):
    post_date = models.DateTimeField('date posted')
    supply = models.CharField(max_length=63)  # This should later be a model as well
    demand = models.CharField(max_length=63)  # This should later be a model as well
    audio_greeting = models.URLField()
    finished = models.BooleanField()

    def __str__(self):
        return "Wants %s for %s, posted at %s" % (self.demand, self.supply, self.post_date)

    def was_posted_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=7) <= self.post_date <= now

    was_posted_recently.admin_order_field = 'pub_date'
    was_posted_recently.boolean = True
    was_posted_recently.short_description = 'Published recently?'

    def is_valid(self):
        return self.was_posted_recently() and not self.finished and self.supply != self.demand

    is_valid.boolean = True
    is_valid.short_description = 'Listing valid?'
