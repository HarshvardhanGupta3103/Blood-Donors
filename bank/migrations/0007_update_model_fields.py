# Generated migration for model field updates

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_donorregistration_aadhar_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorregistration',
            name='last_donate_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='any_disease',
            field=models.CharField(blank=True, default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='allergies',
            field=models.CharField(blank=True, default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='heart_condition',
            field=models.CharField(blank=True, default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='bleeding_disorder',
            field=models.CharField(blank=True, default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='hiv_hcv',
            field=models.CharField(blank=True, default='no', max_length=50),
        ),
        migrations.AlterField(
            model_name='donorregistration',
            name='aadhar_card',
            field=models.ImageField(blank=True, null=True, upload_to='donor_aadhar/'),
        ),
    ]