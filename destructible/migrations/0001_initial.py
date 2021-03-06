# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 20:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(blank=True, max_length=32, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('expire', models.PositiveIntegerField(default=15, validators=[django.core.validators.MaxValueValidator(70, 'The value should be less than %(limit_value)s.')])),
                ('max_expire', models.IntegerField(verbose_name=75)),
                ('password', models.CharField(max_length=32)),
                ('user_name', models.CharField(default='nouser', max_length=100)),
                ('edit_expire_now', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('no_buttons', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_subscribed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='userfile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='destructible.UserFile', verbose_name='UserFile'),
        ),
    ]
