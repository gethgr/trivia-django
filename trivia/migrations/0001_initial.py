# Generated by Django 5.0.1 on 2024-01-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200, null=True)),
                ('option2', models.CharField(max_length=200, null=True)),
                ('option3', models.CharField(max_length=200, null=True)),
                ('option4', models.CharField(max_length=200, null=True)),
                ('correct_answer', models.CharField(max_length=200)),
            ],
        ),
    ]
