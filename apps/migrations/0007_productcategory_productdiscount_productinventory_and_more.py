# Generated by Django 4.2 on 2024-03-24 16:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_user_role_alter_user_uid_alter_useraddress_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('uid', models.CharField(default=uuid.UUID('726c31f0-e639-46ea-be1f-8806b27309a5'), max_length=100, primary_key=True, serialize=False)),
                ('category_name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('uid', models.CharField(default=uuid.UUID('c9b69160-c350-4b7d-85da-38a62c49f54b'), max_length=100, primary_key=True, serialize=False)),
                ('discount_name', models.CharField(max_length=255)),
                ('discount_desc', models.TextField()),
                ('discount_percentage', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('uid', models.CharField(default=uuid.UUID('4af60b8c-faed-46e2-b5b9-098a57c8b4ed'), max_length=100, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='modified_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='modified_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='userrole',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='userrole',
            name='modified_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=uuid.UUID('d8e4b626-d0fe-47c3-87d3-5375671e5d78'), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.CharField(default=uuid.UUID('82594e7f-ecb2-4da6-9e3e-5b005f9689dd'), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='uid',
            field=models.CharField(default=uuid.UUID('92fb2fe6-004a-405d-9150-8adb67b39c27'), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.CharField(default=uuid.UUID('33ddc62b-6d4e-4e8e-8322-1dc3a33d48d4'), max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_desc', models.TextField()),
                ('product_price', models.PositiveBigIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('product_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='apps.productcategory')),
                ('product_discount', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='discount', to='apps.productdiscount')),
                ('product_inventory', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory', to='apps.productinventory')),
            ],
        ),
    ]
