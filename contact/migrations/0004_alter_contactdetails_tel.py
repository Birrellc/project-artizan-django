# Generated by Django 3.2 on 2021-06-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contactdetails_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetails',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]