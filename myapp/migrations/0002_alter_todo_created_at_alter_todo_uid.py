# Generated by Django 4.1.6 on 2023-03-15 12:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1070cfb0-4458-48c1-add8-344ceb3dc5d0'), editable=False, primary_key=True, serialize=False),
        ),
    ]