# Generated by Django 4.1.5 on 2023-01-28 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Afdeling",
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
                ("navn", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="SfoGruppe",
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
                ("gruppe_nummer", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SfoModul",
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
                ("navn", models.CharField(max_length=50)),
                ("pasning_morgen", models.BooleanField()),
                ("pasning_eftermiddag", models.BooleanField()),
                ("pasning_ferier", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("navn", models.CharField(max_length=50)),
                (
                    "afdeling",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.afdeling",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medarbejder",
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
                ("fornavn", models.CharField(max_length=100, verbose_name="fornavn")),
                (
                    "efternavn",
                    models.CharField(max_length=100, verbose_name="efternavn"),
                ),
                (
                    "sfo_gruppe",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.sfogruppe",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Klasse",
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
                ("navn", models.CharField(max_length=50)),
                (
                    "team",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Elev",
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
                ("fornavn", models.CharField(max_length=100)),
                ("efternavn", models.CharField(max_length=100)),
                (
                    "klasse",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.klasse",
                    ),
                ),
                (
                    "sfo_gruppe",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.sfogruppe",
                    ),
                ),
                (
                    "sfomodul",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="skole.sfomodul",
                    ),
                ),
            ],
        ),
    ]
