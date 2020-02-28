# Generated by Django 3.0.3 on 2020-02-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookclub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Occasion', models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Marriage', 'Marriage'), ('Farewell', 'Farewell'), ('Marriage reception', 'Marriage reception'), ('Festival party', 'Festival party')], max_length=25)),
                ('Time_from', models.TimeField()),
                ('Time_to', models.TimeField()),
                ('Date_from', models.DateField()),
                ('Date_to', models.DateField()),
            ],
        ),
    ]
