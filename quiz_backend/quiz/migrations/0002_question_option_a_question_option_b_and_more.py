# Generated by Django 4.2.3 on 2023-11-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_a',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='option_b',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='option_c',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='option_d',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]