# Generated by Django 3.2.13 on 2022-05-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfilio', '0002_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
