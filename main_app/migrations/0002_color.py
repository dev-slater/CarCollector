# Generated by Django 3.2.8 on 2021-10-24 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=150)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='main_app.car')),
            ],
        ),
    ]
