# Generated by Django 4.2.4 on 2023-09-19 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='last_update',
            field=models.DateTimeField(null=True, verbose_name='last update'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='requestor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to=settings.AUTH_USER_MODEL),
        ),
    ]
