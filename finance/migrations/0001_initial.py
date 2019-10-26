# Generated by Django 2.2.6 on 2019-10-26 06:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import finance.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactID', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Номер транзакции')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма оплаты')),
                ('paymentTime', models.DateTimeField(default=datetime.datetime(2019, 10, 26, 11, 11, 58, 862847), verbose_name='Время оплаты')),
                ('terminal', models.CharField(blank=True, max_length=32, null=True, verbose_name='Терминал')),
                ('mfo', models.CharField(max_length=5, verbose_name='МФО банка')),
                ('paymentMethod', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default='offline', max_length=12, null=True, verbose_name='Метод оплаты')),
                ('cheque', models.FileField(null=True, upload_to=finance.models.get_cheque_upload_folder, verbose_name='Чек')),
                ('appType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.App', verbose_name='Название приложение')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.Child', verbose_name='Ф.И.О. воспитанника')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.School')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
