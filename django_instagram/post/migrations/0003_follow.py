# Generated by Django 2.0.2 on 2018-03-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_reple'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folloing', models.CharField(max_length=200)),
                ('follower', models.CharField(max_length=200)),
            ],
        ),
    ]
