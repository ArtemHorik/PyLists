# Generated by Django 4.1.3 on 2022-11-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]