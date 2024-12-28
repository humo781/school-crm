from django.db import models
from django.urls import reverse


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return self.full_name

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:udpate', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])
