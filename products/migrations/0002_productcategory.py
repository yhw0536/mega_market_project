# Generated by Django 4.0 on 2022-01-04 09:30

from django.db import migrations, models

from products.models import ProductCategory


def gen_master(apps, schema_editor):
    ProductCategory(name='구두').save()
    ProductCategory(name='니트').save()
    ProductCategory(name='롱스커트').save()
    ProductCategory(name='숏스커트').save()
    ProductCategory(name='청바지').save()
    ProductCategory(name='자켓').save()
    ProductCategory(name='티셔츠').save()
    ProductCategory(name='코트').save()
    ProductCategory(name='백').save()
    ProductCategory(name='블라우스').save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
            ],
        ),
        migrations.RunPython(gen_master),
    ]
