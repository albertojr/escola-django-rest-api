# Generated by Django 3.2.3 on 2021-05-24 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='cursos.curso'),
        ),
    ]