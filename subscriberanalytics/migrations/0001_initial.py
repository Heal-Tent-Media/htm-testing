# Generated by Django 3.2.5 on 2021-07-22 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccessAnalytic',
            fields=[
                ('admin_name', models.CharField(default='htm-', max_length=30, verbose_name='name')),
                ('admin_id', models.CharField(default='htm-ana-admin-', max_length=20, primary_key=True, serialize=False, verbose_name='admin_id')),
                ('access_hash', models.CharField(default='', max_length=175, verbose_name='access_hash')),
                ('last_req', models.TimeField(default=django.utils.timezone.now, editable=False, verbose_name='last_request')),
                ('total_req', models.CharField(default='', max_length=5, verbose_name='total_requests')),
                ('req_type', models.CharField(default='', max_length=25, verbose_name='request_type')),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceAnalytic',
            fields=[
                ('pref_id', models.CharField(default='', max_length=5, primary_key=True, serialize=False, verbose_name='preference_id')),
                ('sub_id', models.CharField(default='htm-ms-', max_length=15, verbose_name='subscriber_id')),
                ('pref_state', models.CharField(default='', max_length=8, verbose_name='preference_state')),
                ('pref_date', models.DateField(max_length=10, verbose_name='changed_timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='UnsubscriptionAnalytic',
            fields=[
                ('sub_id', models.CharField(default='htm-ms-', max_length=15, primary_key=True, serialize=False, verbose_name='subscriber_id')),
                ('uns_reason', models.CharField(default='unsr-000', max_length=8, verbose_name='unsubscription_reason')),
                ('uns_comment', models.CharField(default='', max_length=150, verbose_name='comments')),
                ('uns_date', models.DateField(max_length=10, verbose_name='unsubscribed_timestamp')),
            ],
        ),
    ]
