# Generated by Django 5.0.3 on 2024-04-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='whatBestSuitsYou',
            field=models.CharField(choices=[('start up', 'start up'), ('company founder', 'company founder'), ('employer', 'employer'), ('other', 'other')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
