# Generated by Django 4.1.5 on 2023-01-17 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('signature_date', models.DateField()),
                ('signed_amount', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.country')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.sector')),
            ],
        ),
    ]
