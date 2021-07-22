# Generated by Django 3.1.1 on 2021-04-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Albumid', models.IntegerField()),
                ('MediaTypeid', models.IntegerField()),
                ('GenreId', models.IntegerField()),
                ('Composer', models.CharField(max_length=200)),
                ('Milllisecs', models.IntegerField()),
                ('Bytes', models.IntegerField()),
                ('unitprice', models.FloatField()),
            ],
        ),
    ]