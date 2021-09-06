# Generated by Django 3.2.6 on 2021-09-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_auto_20210902_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('research_early_access', 'Research early access'),),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
