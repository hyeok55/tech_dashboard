# Generated by Django 4.2.7 on 2023-11-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("techs", "0004_alter_company_company_name_alter_tag_tag_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company_tag",
            name="updates",
            field=models.DateTimeField(auto_now=True, verbose_name="업데이트 날짜"),
        ),
        migrations.AlterField(
            model_name="post",
            name="url",
            field=models.TextField(unique=False, verbose_name="링크"),
        ),
    ]