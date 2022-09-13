# Generated by Django 4.0.2 on 2022-02-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('machine', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('ps', models.CharField(max_length=255)),
                ('most_bonus', models.CharField(max_length=255)),
                ('probability', models.CharField(max_length=255)),
                ('BB_probability', models.CharField(max_length=255)),
                ('RB_probability', models.CharField(max_length=255)),
                ('cumulative_start', models.CharField(max_length=255)),
                ('yesterday_start', models.CharField(max_length=255)),
                ('last_value', models.CharField(max_length=255)),
                ('table', models.TextField()),
                ('graph', models.TextField()),
                ('shop_id', models.IntegerField(max_length=10)),
                ('machine_id', models.IntegerField(max_length=10)),
                ('unit_id', models.IntegerField(max_length=10)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'data',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('machine', models.CharField(max_length=255)),
                ('ps', models.CharField(max_length=255)),
                ('shop_id', models.IntegerField(max_length=10)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'machine',
            },
        ),
        migrations.CreateModel(
            name='Pachinko',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('machine', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('most_bonus', models.CharField(max_length=255)),
                ('probability', models.CharField(max_length=255)),
                ('cumulative_start', models.CharField(max_length=255)),
                ('yesterday_start', models.CharField(max_length=255)),
                ('last_value', models.CharField(max_length=255)),
                ('table', models.TextField()),
                ('graph', models.TextField()),
                ('shop_id', models.IntegerField(max_length=10)),
                ('machine_id', models.IntegerField(max_length=10)),
                ('unit_id', models.IntegerField(max_length=10)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'pachinko',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('pachinko_rate', models.CharField(max_length=255)),
                ('slot_rate', models.CharField(max_length=255)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('machine', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('most_bonus', models.CharField(max_length=255)),
                ('probability', models.CharField(max_length=255)),
                ('BB_probability', models.CharField(max_length=255)),
                ('RB_probability', models.CharField(max_length=255)),
                ('cumulative_start', models.CharField(max_length=255)),
                ('yesterday_start', models.CharField(max_length=255)),
                ('last_value', models.CharField(max_length=255)),
                ('table', models.TextField()),
                ('graph', models.TextField()),
                ('shop_id', models.IntegerField(max_length=10)),
                ('machine_id', models.IntegerField(max_length=10)),
                ('unit_id', models.IntegerField(max_length=10)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'slot',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('machine', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('ps', models.CharField(max_length=255)),
                ('shop_id', models.IntegerField(max_length=10)),
                ('machine_id', models.IntegerField(max_length=10)),
                ('created_by_id', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'unit',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('verfied', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
