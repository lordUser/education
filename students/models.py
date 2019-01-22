from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField(max_length=200)
    ticket = models.IntegerField(primary_key=True)
    group = models.ForeignKey('StudentGroup',
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class StudentGroup(models.Model):
    name = models.CharField(max_length=200)
    captain = models.ForeignKey('Student',
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
