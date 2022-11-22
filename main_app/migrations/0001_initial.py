# Generated by Django 4.1.3 on 2022-11-21 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.CharField(max_length=2000)),
                ('directions', models.TextField(max_length=2000)),
                ('description', models.TextField(max_length=500)),
                ('region', models.CharField(choices=[('NA', 'North America'), ('SA', 'South America'), ('CA', 'Central America'), ('EU', 'Europe'), ('AS', 'Asia'), ('ME', 'Middle East'), ('AF', 'Africa'), ('OC', 'Oceania')], default='NA', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]