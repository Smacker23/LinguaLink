# Generated by Django 4.2.18 on 2025-02-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_rename_original_word_question_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='quiz.tag'),
        ),
    ]
