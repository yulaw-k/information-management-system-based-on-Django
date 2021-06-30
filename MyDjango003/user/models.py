from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PersonInfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    number = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'


class Schedule(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    beginDate = models.DateField()
    endDate = models.DateField()
    person = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '日程信息'
