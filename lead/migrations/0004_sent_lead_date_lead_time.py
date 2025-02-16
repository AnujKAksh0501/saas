# Generated by Django 5.1.4 on 2025-02-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_rename_mobile_lead_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('to_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
