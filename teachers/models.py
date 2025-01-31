from django.db import models
from django.urls import reverse
from subjects.models import Subject


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name='teachers')
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    experience = models.FloatField()
    image = models.ImageField(upload_to='teacher_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])
