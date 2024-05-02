from django.db import models

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    subjects = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.TextField()
    state = models.BooleanField()

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField()
    answers = models.ForeignKey('Answer', on_delete=models.PROTECT, null=True)
    category = models.TextField()

    def __str__(self):
        return self.text


class QuestionShort(models.Model):
    text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.pk


class TestShort(models.Model):
    name = models.TextField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('Teachers', on_delete=models.DO_NOTHING, null=True)
    questions = models.ManyToManyField(QuestionShort)


class Test(models.Model):
    questions = models.ForeignKey('Question', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    students = models.ForeignKey('Students', on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey('Teachers', on_delete=models.DO_NOTHING, null=True)
