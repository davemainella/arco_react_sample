# Generated by Django 3.1.5 on 2021-01-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210115_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('med', 'Medium'), ('low', 'Low')], default='med', max_length=4, null=True),
        ),
    ]