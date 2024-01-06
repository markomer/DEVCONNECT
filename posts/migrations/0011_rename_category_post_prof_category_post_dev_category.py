# Generated by Django 4.0.5 on 2022-07-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_post_header_image_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='prof_category',
        ),
        migrations.AddField(
            model_name='post',
            name='dev_category',
            field=models.CharField(default='all', max_length=255),
        ),
    ]
