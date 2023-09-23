# Generated by Django 4.2.5 on 2023-09-23 11:49

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_book_have'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book_have',
        ),
        migrations.AddField(
            model_name='book',
            name='student_have',
            field=models.ForeignKey(null=True, on_delete=builtins.callable, to='home.student'),
        ),
    ]