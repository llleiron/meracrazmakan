# Generated by Django 3.0.3 on 2020-04-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Գրանցում',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ազգանուն', models.CharField(blank=True, max_length=32, null=True, verbose_name='Ազգանուն')),
                ('Անուն', models.CharField(blank=True, max_length=32, null=True, verbose_name='Անուն')),
                ('Հայրանուն', models.CharField(blank=True, max_length=32, null=True, verbose_name='Հայրանուն')),
                ('ԳրանցմանԱմսաթիվ', models.DateField(auto_now=True, null=True, verbose_name='Գրանցման ամսաթիվ')),
            ],
        ),
    ]
