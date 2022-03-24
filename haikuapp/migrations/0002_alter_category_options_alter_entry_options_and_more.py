# Generated by Django 4.0.3 on 2022-03-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='entry_status',
            options={'verbose_name_plural': 'Entry Status'},
        ),
        migrations.AlterModelOptions(
            name='haiku',
            options={'verbose_name_plural': 'Haiku'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_status',
            field=models.CharField(choices=[('hide', 'hide'), ('show', 'show')], max_length=45),
        ),
        migrations.AlterField(
            model_name='entry',
            name='haiku_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entry_status',
            name='entry_status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('rejected', 'rejected')], max_length=45),
        ),
    ]
