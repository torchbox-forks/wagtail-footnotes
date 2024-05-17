# Generated by Django 4.2.9 on 2024-01-11 12:58

import uuid

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("wagtail_footnotes", "0004_boostrap_translatable_mixin_data_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footnote",
            name="locale",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.locale",
            ),
        ),
        migrations.AlterField(
            model_name="footnote",
            name="translation_key",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
