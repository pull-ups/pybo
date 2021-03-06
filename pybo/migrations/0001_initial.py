# Generated by Django 3.2.5 on 2021-08-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('category', models.TextField(choices=[('인사', '인사게시판'), ('질문', '질문게시판'), ('정보', '정보게시판')], default='')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.article')),
            ],
        ),
    ]
