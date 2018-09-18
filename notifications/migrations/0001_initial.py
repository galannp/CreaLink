# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('notif_type', models.CharField(max_length=500, default='Comment on Subject', choices=[('subject_mentioned', 'Mentioned in Subject'), ('comment_mentioned', 'Mentioned in Comment'), ('comment', 'Comment on Subject'), ('follow', 'Followed by someone'), ('sent_msg_request', 'Sent a Message Request'), ('confirmed_msg_request', 'Sent a Message Request')])),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Actor', models.ForeignKey(related_name='c_acts', to=settings.AUTH_USER_MODEL)),
                ('Object', models.ForeignKey(blank=True, null=True, related_name='act_notif', to='subjects.Subject')),
                ('Target', models.ForeignKey(related_name='c_notif', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]