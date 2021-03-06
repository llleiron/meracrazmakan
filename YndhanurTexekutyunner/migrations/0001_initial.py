# Generated by Django 3.0.3 on 2020-04-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grancum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ԸնդհանուրՏեղեկություններ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Զինկոչումը', models.CharField(blank=True, max_length=32, null=True, verbose_name='Զինկոչումը')),
                ('ԱրյանԽումբը', models.CharField(blank=True, max_length=32, null=True, verbose_name='Արյան խումբը')),
                ('ԾննդյանՏարեթիվը', models.DateField(blank=True, null=True, verbose_name='Ծննդյան տարեթիվը')),
                ('Ազգությունը', models.CharField(blank=True, max_length=32, null=True, verbose_name='Ազգությունը')),
                ('Կրթությունը', models.CharField(blank=True, help_text='ընդհանուր, զինվորական, հատուկ մասնագիտական', max_length=300, null=True, verbose_name='Կրթությունը')),
                ('ԾառայությանԱնցնելուԱմսաթիվը', models.DateField(blank=True, null=True, verbose_name='Ծառայության անցնելու ամսաթիվը')),
                ('ԸնտանեկանԴրությունը', models.TextField(blank=True, help_text='ամուրի, ամուսնացած, երեխաների և խնամակյալների թիվը', max_length=300, null=True, verbose_name='Ընտանեկան դրություն')),
                ('ՏանՀասցեն', models.CharField(blank=True, max_length=300, null=True, verbose_name='Տան հասցեն')),
                ('ՏանՀեռախոսահամարը', models.IntegerField(blank=True, help_text='+***********', null=True, verbose_name='Տան հեռախոսահամարը')),
                ('ԾառայավայրիՀասցեն', models.TextField(blank=True, max_length=300, null=True, verbose_name='Ծառայավայրի հասցեն')),
                ('ԾառայավայրիՀեռախոսահամարը', models.IntegerField(blank=True, help_text='+***********', null=True, verbose_name='Ծառայավայրի հեռախոսահամարը')),
                ('հհ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում')),
            ],
        ),
    ]
