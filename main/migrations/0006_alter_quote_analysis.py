# Generated by Django 3.2 on 2022-03-04 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220304_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='analysis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quoteanalysis'),
        ),
    ]
