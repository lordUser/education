# Generated by Django 2.1.5 on 2019-01-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(max_length=200)),
                ('ticket', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('captain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.StudentGroup'),
        ),
    ]