# Generated by Django 4.1 on 2024-12-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automates_app', '0010_remove_draft_generated_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='generated_description',
            field=models.TextField(default=''),
        ),
    ]
