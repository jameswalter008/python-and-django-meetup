# Generated by Django 3.2.6 on 2021-09-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_auto_20210916_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-9-20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='2021-9-20', max_length=254),
            preserve_default=False,
        ),
    ]