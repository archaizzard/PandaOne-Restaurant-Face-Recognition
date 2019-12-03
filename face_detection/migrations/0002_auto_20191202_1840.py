# Generated by Django 3.0 on 2019-12-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='regularcustomer',
            name='age',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_visit',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of first visit'),
        ),
        migrations.AddField(
            model_name='customer',
            name='spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='mixinregularcustomerinfo',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='mixinregularcustomerinfo',
            name='favorite_table',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='regularcustomer',
            name='first_visit',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of first visit'),
        ),
        migrations.AddField(
            model_name='regularcustomer',
            name='spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='mixinregularcustomerinfo',
            name='has_pet',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='regularcustomer',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
