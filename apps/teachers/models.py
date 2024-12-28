from django.db import models
from django.urls import reverse

from apps.subjects.models import Subject

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name='teachers')
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField()
    image = models.ImageField(upload_to='teacher_image/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:udpate', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])
