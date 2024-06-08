# Generated by Django 3.2.5 on 2024-06-02 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='Choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='Question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Question_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
