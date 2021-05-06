# Generated by Django 3.2.1 on 2021-05-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callKey', models.CharField(blank=True, max_length=200, null=True)),
                ('disposition', models.CharField(blank=True, max_length=200, null=True)),
                ('hangupcause', models.CharField(blank=True, max_length=200, null=True)),
                ('assigned', models.BooleanField(default=True)),
            ],
        ),
    ]