# Generated by Django 3.1.4 on 2021-03-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210323_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='slugger', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
