# Generated by Django 2.0.2 on 2018-04-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20180324_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reple',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='reple',
            name='author_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reple',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
