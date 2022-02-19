# Generated by Django 4.0.2 on 2022-02-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name_surname', models.CharField(max_length=150)),
                ('owner_age', models.IntegerField()),
                ('owner_mail', models.EmailField(max_length=200)),
                ('owner_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_familia', models.CharField(max_length=100)),
                ('pet_species', models.CharField(max_length=100)),
                ('pet_name', models.CharField(max_length=150)),
                ('pet_age', models.IntegerField()),
                ('pet_description', models.TextField(blank=True, max_length=1000)),
                ('the_owner_of_pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets_and_owners.owner_data')),
            ],
        ),
    ]