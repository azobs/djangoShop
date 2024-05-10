# Generated by Django 5.0.4 on 2024-05-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_rename_name_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='Store_categ_name_968de2_idx'),
        ),
    ]
