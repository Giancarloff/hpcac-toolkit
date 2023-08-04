# Generated by Django 4.2.1 on 2023-07-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clusters", "0004_alter_clusterconfiguration_cloud_provider"),
    ]

    operations = [
        migrations.AddField(
            model_name="clusterconfiguration",
            name="nodes",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clusterconfiguration",
            name="transient",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="clusterconfiguration",
            name="username",
            field=models.TextField(default="ec2-user"),
        ),
    ]