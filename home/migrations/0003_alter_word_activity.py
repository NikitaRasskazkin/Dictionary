# Generated by Django 3.2.8 on 2021-10-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_word_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='activity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.activity'),
        ),
    ]