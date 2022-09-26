# Generated by Django 4.1.1 on 2022-09-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="difficulty",
            field=models.CharField(
                choices=[("B", "Beginner"), ("I", "Intermediate"), ("A", "Advanced")],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="title",
            field=models.TextField(),
        ),
    ]