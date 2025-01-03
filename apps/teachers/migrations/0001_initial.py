# Generated by Django 5.1.4 on 2024-12-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('experience', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='teacher_image/')),
                ('subject', models.ManyToManyField(related_name='teachers', to='subjects.subject')),
            ],
        ),
    ]
