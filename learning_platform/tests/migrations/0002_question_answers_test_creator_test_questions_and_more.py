# Generated by Django 5.0.3 on 2024-04-20 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tests.answer'),
        ),
        migrations.AddField(
            model_name='test',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tests.teachers'),
        ),
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tests.question'),
        ),
        migrations.AddField(
            model_name='test',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tests.students'),
        ),
    ]
