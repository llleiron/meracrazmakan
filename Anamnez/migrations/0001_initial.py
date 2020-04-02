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
            name='Անամնեզ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ՀիվանդացելԷ', models.TextField(blank=True, help_text='հիվանդությունը, որ տարիքում', max_length=1000, null=True, verbose_name='1․ Հիվանդացել է')),
                ('վիրավորումները', models.TextField(blank=True, max_length=1000, null=True, verbose_name='2․ա) վիրավորումները')),
                ('Կոնտուզիաները', models.TextField(blank=True, max_length=1000, null=True, verbose_name='2․բ) կոնտուզիաները')),
                ('Վիրահատությունները', models.TextField(blank=True, max_length=1000, null=True, verbose_name='3․ Վիրահատությունները')),
                ('ԱրձակուրդներըՀիվանդությանՊատճառով', models.TextField(blank=True, max_length=1000, null=True, verbose_name='4. Արձակուրդները հիվանդությունների պատճառով')),
                ('ԲուժումնԱռողջարաններում', models.TextField(blank=True, max_length=1000, null=True, verbose_name='5. Բուժումն առողջարաններում')),
                ('Ժառանգականությունը', models.TextField(blank=True, help_text='ընտանեկան անամնեզ', max_length=1000, null=True, verbose_name='6. Ժառանգականությունը')),
                ('ԻնչԴեղերՉիԿարողանումԸնդունել', models.TextField(blank=True, max_length=1000, null=True, verbose_name='7. Ինչ դեղեր չի կարողանում ընդունել')),
                ('ՆերարկումներիԱզդեցությունը', models.TextField(blank=True, help_text='օրգանիզմի արձագանքը', max_length=1000, null=True, verbose_name='8. Ներարկումների ազդեցությունը')),
                ('ՎնասակարՍովորությունները', models.TextField(blank=True, help_text='խմել, ծխել և այլն', max_length=1000, null=True, verbose_name='9. Վնասակար սովորությունները')),
                ('ՀատուկՆշումներ', models.TextField(blank=True, max_length=1000, null=True, verbose_name='10. Հատուկ նշումներ')),
                ('հհ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում')),
            ],
        ),
    ]
