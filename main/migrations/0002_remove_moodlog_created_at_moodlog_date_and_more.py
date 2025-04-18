# Generated by Django 5.1.3 on 2024-11-24 02:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodlog',
            name='created_at',
        ),
        migrations.AddField(
            model_name='moodlog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='moodlog',
            name='mood',
            field=models.CharField(choices=[('happy', 'Happy'), ('neutral', 'Neutral'), ('sad', 'Sad'), ('angry', 'Angry'), ('anxious', 'Anxious')], max_length=50),
        ),
        migrations.DeleteModel(
            name='TherapistSession',
        ),
    ]
