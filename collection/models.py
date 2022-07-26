from django.db import models

class Count(models.Model):
    counter = models.TextField(primary_key=True, blank=True)  # This field type is a guess.
    count_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'count'

class Tweets(models.Model):
    index = models.TextField(primary_key=True, blank=True)  # This field type is a guess.
    player = models.TextField(blank=True, null=True)  # This field type is a guess.
    tweet = models.TextField(blank=True, null=True)  # This field type is a guess.
    score = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'tweets'
