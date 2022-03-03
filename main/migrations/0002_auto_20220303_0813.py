# Generated by Django 3.2 on 2022-03-03 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteanalysis',
            name='longest_words',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quoteanalysis',
            name='quote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.quote'),
            preserve_default=False,
        ),
    ]