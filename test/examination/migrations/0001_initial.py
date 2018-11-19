# Generated by Django 2.1.1 on 2018-11-14 08:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_subject', models.CharField(max_length=10)),
                ('user_key', models.CharField(max_length=255, unique=True)),
                ('questions', models.CharField(max_length=255)),
                ('choices', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_ans', models.CharField(max_length=255)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TermSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('term_start', models.DateField(default=datetime.date.today)),
                ('term_end', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.SubjectCategories'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_question',
            field=models.ManyToManyField(related_name='subjectquestion', through='examination.Question', to='examination.TermSession'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.TermSession'),
        ),
        migrations.AddField(
            model_name='question',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.SubjectCategories'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='examination.Subject'),
        ),
        migrations.AddField(
            model_name='question',
            name='term_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.TermSession'),
        ),
    ]
