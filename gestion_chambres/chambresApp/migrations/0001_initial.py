# Generated by Django 5.0 on 2023-12-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=13)),
                ('price', models.BigIntegerField()),
                ('date_entre', models.DateField()),
                ('date_sortie', models.DateField()),
            ],
        ),
    ]