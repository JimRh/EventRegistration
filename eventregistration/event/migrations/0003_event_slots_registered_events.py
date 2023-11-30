# Generated by Django 4.2.7 on 2023-11-28 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0002_remove_event_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slots',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Registered_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('participants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]