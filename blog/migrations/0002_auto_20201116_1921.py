# Generated by Django 3.0 on 2020-11-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occurence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('genus', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('distribution', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='species',
            old_name='name',
            new_name='query',
        ),
    ]