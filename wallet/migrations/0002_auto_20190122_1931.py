# Generated by Django 2.1.5 on 2019-01-22 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smob', models.IntegerField(max_length=11)),
                ('tdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(max_length=100000)),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='id',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='rmob',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='transactions_log',
            name='rmob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Transactions'),
        ),
        migrations.AddField(
            model_name='transactions_log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
