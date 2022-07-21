# Generated by Django 2.2.16 on 2022-07-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_from', models.CharField(max_length=3)),
                ('name_to', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
