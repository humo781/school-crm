from django.db import models
from django.urls import reverse
from groups.models import Group


class Student(models.Model):
    group = models.ForeignKey(Group,  on_delete=models.CASCADE, related_name='students', default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_of_date = models.DateField()
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])
