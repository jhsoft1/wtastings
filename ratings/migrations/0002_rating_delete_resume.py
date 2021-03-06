# Generated by Django 4.0 on 2022-01-21 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nose', models.IntegerField()),
                ('taste', models.IntegerField()),
                ('color', models.IntegerField()),
                ('smokiness', models.IntegerField()),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
