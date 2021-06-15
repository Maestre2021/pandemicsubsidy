# Generated by Django 3.1.6 on 2021-06-15 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psrstatus',
            name='p_status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='prac.psrsignup'),
        ),
        migrations.AlterField(
            model_name='inquries',
            name='rate',
            field=models.CharField(choices=[('3', 'good'), ('5', 'excellent'), ('1', 'poor'), ('2', 'weak'), ('4', 'very good')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='psrstatus',
            name='stat',
            field=models.CharField(choices=[('DENIED', 'denied'), ('PENDING', 'pending'), ('RECEIVED', 'received')], default='', max_length=20),
        ),
    ]
