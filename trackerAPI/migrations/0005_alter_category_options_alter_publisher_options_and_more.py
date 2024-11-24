# Generated by Django 5.1.3 on 2024-11-23 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerAPI', '0004_alter_book_category_alter_book_publisher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.ManyToManyField(to='trackerAPI.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
