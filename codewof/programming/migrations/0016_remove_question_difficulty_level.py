# Generated by Django 3.2.11 on 2022-04-17 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0015_question_difficulty_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='difficulty_level',
        ),
    ]
