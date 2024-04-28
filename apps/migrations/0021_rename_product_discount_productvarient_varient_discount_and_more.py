# Generated by Django 4.2 on 2024-04-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_alter_accesslog_uid_alter_cartitem_uid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvarient',
            old_name='product_discount',
            new_name='varient_discount',
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='uid',
            field=models.CharField(default='3889721d73db48fea4677efbed8a5282171354041813282', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='uid',
            field=models.CharField(default='09541df72a3b4a2f990007bdafc14739171354041861648', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='uid',
            field=models.CharField(default='e038fc6745cd407fb3040805a26ee03c171354041850612', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uid',
            field=models.CharField(default='b0339ae2519444b0881714f6a6e5325e171354041895535', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='345a978598b64502948de48ce8a1bea0171354041864910', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='uid',
            field=models.CharField(default='7eec4c372c354e8ea944ba7536ace3e0171354041850324', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(default='a3b1f410e06740879a639d31a7b4e662171354041815331', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productattachment',
            name='uid',
            field=models.CharField(default='21e8e6c6b3d64b6eaaaa051b2af6d70d171354041851829', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='uid',
            field=models.CharField(default='197a2343e0fd4cc5adc89639c9b307bb171354041889876', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='uid',
            field=models.CharField(default='9a738ba7b63d49d9995f2124f7ac2fa2171354041826952', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='uid',
            field=models.CharField(default='6abee68119a64e3b813a15d918bf1965171354041863412', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productordertodeliverystatus',
            name='uid',
            field=models.CharField(default='2de6f475b4084802b9c654db9efb3ed7171354041842058', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productvarient',
            name='uid',
            field=models.CharField(default='03bdbbd04da2482fa6e1671c7e1dedf6171354041837678', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='f001aa00374a4da99f60d37d3e87d54f171354041896422', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.CharField(default='30f3ac34042d40ceadd927c20977001c171354041826477', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='uid',
            field=models.CharField(default='6eca940072de4621b0837fa857167c0b171354041860675', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='variantoptions',
            name='uid',
            field=models.CharField(default='1cb4c7c2a64e484fb430dfb7ce7bfc8a171354041842517', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='varientattribute',
            name='uid',
            field=models.CharField(default='90bbf627da534ce79cf0eb3251e44d4c171354041848605', max_length=255, primary_key=True, serialize=False),
        ),
    ]
