# Generated by Django 4.1.3 on 2022-12-10 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]