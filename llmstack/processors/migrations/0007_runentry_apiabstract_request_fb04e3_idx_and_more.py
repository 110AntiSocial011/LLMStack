# Generated by Django 4.2.11 on 2024-04-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiabstractor', '0006_remove_share_api_backend_remove_share_owner_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='runentry',
            index=models.Index(fields=['request_uuid'], name='apiabstract_request_fb04e3_idx'),
        ),
        migrations.AddIndex(
            model_name='runentry',
            index=models.Index(fields=['app_uuid'], name='apiabstract_app_uui_4dfd2a_idx'),
        ),
        migrations.AddIndex(
            model_name='runentry',
            index=models.Index(fields=['app_store_uuid'], name='apiabstract_app_sto_1896c3_idx'),
        ),
        migrations.AddIndex(
            model_name='runentry',
            index=models.Index(fields=['session_key'], name='apiabstract_session_316e25_idx'),
        ),
    ]
