# Generated by Django 2.0.1 on 2018-02-26 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.SmallIntegerField(choices=[(0, 'Starters'), (1, 'Mocktail'), (2, 'Lunch'), (3, 'Dinner')], default=None)),
                ('dish_name', models.CharField(max_length=100)),
                ('about', models.TextField(blank=True, null=True)),
                ('combo_avail', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('image_url', models.CharField(blank=True, default='', max_length=200)),
                ('dish_status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.SmallIntegerField(choices=[(0, 'Regular'), (1, 'Valentine'), (2, 'Diwali'), (3, 'Christmas'), (4, 'New_Year_Eve'), (5, 'Others')], default=0)),
                ('offer_perc', models.PositiveIntegerField(default=0)),
                ('offer_tnc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='offers_avail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dish.Offers'),
        ),
        migrations.AddField(
            model_name='combo',
            name='dish1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish1', to='dish.Menu', unique=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='dish2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish2', to='dish.Menu', unique=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='dish3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish3', to='dish.Menu', unique=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='dish4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish4', to='dish.Menu', unique=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='dish5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish5', to='dish.Menu', unique=True),
        ),
    ]
