# Generated by Django 4.2.1 on 2023-05-29 13:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clusters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MPIExperiment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.TextField(unique=True)),
                ("github_repository", models.URLField()),
                (
                    "ft_strategy",
                    models.CharField(
                        choices=[
                            ("BLCR", "Berkeley-Labs Checkpoint/Restart"),
                            ("ULFM", "User-Level Failure Mitigation"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("starting", "Starting"),
                            ("running", "Running"),
                            ("checkpointing", "Checkpointing"),
                            ("restarting", "Restarting"),
                            ("completed", "Completed"),
                        ],
                        default="starting",
                        max_length=20,
                    ),
                ),
                ("started_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("completed_at", models.DateTimeField(null=True)),
                (
                    "cluster_configuration",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="clusters.clusterconfiguration",
                    ),
                ),
            ],
        ),
    ]