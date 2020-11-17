# Generated by Django 3.1 on 2020-11-17 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpage', '0002_auto_20201116_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='user_image'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userpage.post')),
                ('user', models.ManyToManyField(related_name='linkingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
