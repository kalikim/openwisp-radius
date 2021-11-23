# Generated by Django 4.0rc1 on 2021-11-23 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_users', '0004_user_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(
                related_name='%(app_label)s_%(class)s',
                through='sample_users.OrganizationUser',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='organizationuser',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='%(app_label)s_%(class)s',
                to='sample_users.user',
            ),
        ),
    ]