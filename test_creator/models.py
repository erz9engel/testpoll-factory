from django.db import models


class TestQuestions(models.Model):
    question = models.TextField()
    answers_quantity = models.PositiveSmallIntegerField()
    correct_answer = models.PositiveSmallIntegerField()
    topic = models.CharField(max_length=50, blank=True)
    published = models.BooleanField(default=False)
    file_id = models.CharField(max_length=64, blank=True)
    explanation_link = models.URLField(blank=True)


class Polls(models.Model):
    test_question = models.ForeignKey('testquestions', on_delete=models.DO_NOTHING)
    msg_id = models.PositiveSmallIntegerField()
    channel = models.ForeignKey('channels', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('channel', 'msg_id')


class Users(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(max_length=32, blank=True)
    registered = models.DateField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    is_moderator = models.BooleanField(default=False)


class Votings(models.Model):
    voter = models.ForeignKey('users', on_delete=models.DO_NOTHING)
    poll = models.ForeignKey('polls', on_delete=models.DO_NOTHING)
    voted_for = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('voter', 'poll')


class Schedule(models.Model):
    testquestion = models.ForeignKey('voters', on_delete=models.CASCADE)
    planned_time = models.DateTimeField()
    channel = models.ForeignKey('channels', on_delete=models.CASCADE)


class Channels(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=32)
    moderators = models.ManyToManyField(Users)
