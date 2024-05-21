# Generated by Django 5.0.6 on 2024-05-21 08:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecfood_dish', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecfood_dish.dish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
