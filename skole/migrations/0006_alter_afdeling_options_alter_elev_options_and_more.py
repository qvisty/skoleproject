# Generated by Django 4.1.5 on 2023-01-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skole", "0005_alter_afdeling_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="afdeling",
            options={
                "ordering": ["navn"],
                "verbose_name": "afdeling",
                "verbose_name_plural": "afdelinger",
            },
        ),
        migrations.AlterModelOptions(
            name="elev",
            options={
                "ordering": ["fornavn", "efternavn"],
                "verbose_name": "elev",
                "verbose_name_plural": "elever",
            },
        ),
        migrations.AlterModelOptions(
            name="medarbejder",
            options={
                "ordering": ["fornavn", "efternavn"],
                "verbose_name": "medarbejder",
                "verbose_name_plural": "medarbejdere",
            },
        ),
        migrations.AlterField(
            model_name="sfogruppe",
            name="gruppe_nummer",
            field=models.CharField(max_length=1),
        ),
    ]
