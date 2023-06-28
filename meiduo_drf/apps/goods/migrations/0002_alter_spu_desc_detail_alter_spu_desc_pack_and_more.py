# Generated by Django 4.1.7 on 2023-06-27 13:35

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spu',
            name='desc_detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='详细介绍'),
        ),
        migrations.AlterField(
            model_name='spu',
            name='desc_pack',
            field=ckeditor.fields.RichTextField(default='', verbose_name='包装信息'),
        ),
        migrations.AlterField(
            model_name='spu',
            name='desc_service',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='售后服务'),
        ),
    ]
