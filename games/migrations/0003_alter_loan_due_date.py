# Generated by Django 5.1.3 on 2024-11-06 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_loan_due_date_alter_loan_borrowed_at_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 20, 23, 16, 11, 165638, tzinfo=datetime.timezone.utc)),
        ),
    ]
