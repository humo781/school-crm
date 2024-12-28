from django.db import models
from django.urls import reverse
from apps.teachers.models import Teacher
from apps.students.models import Student


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])
