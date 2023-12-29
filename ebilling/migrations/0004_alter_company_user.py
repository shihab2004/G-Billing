# Generated by Django 4.1.1 on 2022-10-20 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ebilling", "0003_remove_company_user_company_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="user",
            field=models.ManyToManyField(
                blank=True, related_name="getCompany", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
