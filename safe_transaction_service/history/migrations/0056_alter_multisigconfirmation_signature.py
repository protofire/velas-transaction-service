# Generated by Django 3.2.12 on 2022-03-21 09:59

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0055_alter_multisigtransaction_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multisigconfirmation",
            name="signature",
            field=gnosis.eth.django.models.HexField(
                default=None, max_length=5000, null=True
            ),
        ),
    ]
