# Generated by Django 3.0.7 on 2020-07-25 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yummyNUS', '0002_auto_20200726_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='Foodstall',
        ),
        migrations.AddField(
            model_name='foodstall',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yummyNUS.Review'),
        ),
    ]
