# Generated by Django 3.0.2 on 2020-02-06 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(blank=True, max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='iv_item_specification',
            new_name='category',
        ),
        migrations.DeleteModel(
            name='iv_items',
        ),
        migrations.AddField(
            model_name='foods',
            name='category_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.category'),
        ),
    ]
