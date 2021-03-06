# Generated by Django 3.2.5 on 2021-07-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailSubscriber',
            fields=[
                ('ms_id', models.CharField(default='htm-ms-', max_length=15, primary_key=True, serialize=False, verbose_name='id')),
                ('ms_mail', models.CharField(default='Mail', max_length=100, verbose_name='subscriber_mail')),
                ('ms_verification_status', models.BooleanField(default=False, max_length=5, verbose_name='verification_status')),
                ('ms_mail_verify_hash', models.CharField(default='', max_length=175, verbose_name='mail_verification_hash')),
                ('ms_unsubscribe_hash', models.CharField(default='', max_length=175, verbose_name='unsubscription_hash')),
                ('ms_preference_hash', models.CharField(default='', max_length=175, verbose_name='preference_hash')),
                ('ms_info_mail_status', models.BooleanField(default=False, max_length=5, verbose_name='info_mail_status')),
                ('ms_promotional_mail_status', models.BooleanField(default=False, max_length=5, verbose_name='promotional_mail_status')),
                ('ms_update_mail_status', models.BooleanField(default=True, max_length=5, verbose_name='update_mail_status')),
                ('ms_sub_status', models.BooleanField(default=False, max_length=5, verbose_name='subscription_status')),
                ('ms_sub_date', models.DateField(max_length=10, verbose_name='subscribed_timestamp')),
                ('ms_unsub_date', models.DateField(max_length=10, null=True, verbose_name='unsubscribed_timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesList',
            fields=[
                ('svc_name', models.CharField(default='Heal Tent Service', max_length=50, verbose_name='service_name')),
                ('svc_tagline', models.CharField(default='Service Tagline', max_length=100, verbose_name='service_tagline')),
                ('svc_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='service_id')),
                ('svc_ic_url', models.CharField(max_length=200, verbose_name='service_ic_url')),
                ('svc_des_sh', models.CharField(max_length=160, verbose_name='service_des_short')),
                ('svc_des_lo', models.TextField(max_length=1500, verbose_name='service_des_long')),
                ('svc_req_url', models.CharField(max_length=200, verbose_name='service_request_url')),
            ],
        ),
        migrations.CreateModel(
            name='TeamDetails',
            fields=[
                ('tm_id', models.CharField(default='htm-', max_length=10, verbose_name='id')),
                ('tm_name', models.CharField(default='Name', max_length=50, primary_key=True, serialize=False, verbose_name='name')),
                ('tm_des', models.CharField(default='Designation', max_length=50, verbose_name='designation')),
                ('tm_profile', models.URLField(default='Profile URL', verbose_name='profile_url')),
                ('linkedin_id', models.CharField(default='https://www.linkedin.com/in/', max_length=70, verbose_name='linkedin')),
                ('instagram_id', models.CharField(default='https://www.instagram.com/', max_length=70, verbose_name='instagram')),
                ('twitter_id', models.CharField(default='https://twitter.com/', max_length=70, verbose_name='twitter')),
            ],
        ),
    ]
