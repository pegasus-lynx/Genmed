# Generated by Django 2.1.1 on 2018-11-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('comment_no', models.IntegerField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
