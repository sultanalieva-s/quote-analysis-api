# Generated by Django 3.2 on 2022-03-04 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_quoteanalysis_average_word_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteanalysis',
            name='quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='analysis',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.quoteanalysis'),
            preserve_default=False,
        ),
    ]
