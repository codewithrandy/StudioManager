# Generated by Django 4.1.5 on 2023-01-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
                ('revenue', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=100, null=True)),
            ],
        ),
    ]
