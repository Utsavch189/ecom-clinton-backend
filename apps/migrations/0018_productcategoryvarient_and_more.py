# Generated by Django 4.2 on 2024-04-19 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_accesslog_product_product_brand_alter_cartitem_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryVarient',
            fields=[
                ('uid', models.CharField(default='99cc12e3c86346cba0c19e52c833f162171351021119335', max_length=255, primary_key=True, serialize=False)),
                ('varient_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_inventory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='uid',
            field=models.CharField(default='bf423b47f03d4dd38373c9a0ac6ee136171351021113385', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='uid',
            field=models.CharField(default='c535eeef2cbf47709ce0977692d0b62f171351021157607', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='uid',
            field=models.CharField(default='19972fef83ae4fccad73625413977f85171351021160061', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uid',
            field=models.CharField(default='1cf395943ae24eec92915a8c283240f8171351021156421', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='55230c2882b24ee1be242c89ac534365171351021119489', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='uid',
            field=models.CharField(default='1a5499b12dd342adb09236e68715af84171351021196754', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(default='98c20cfd2b8e4f67b1647f67c21d810a171351021170852', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productattachment',
            name='uid',
            field=models.CharField(default='5d4d1efc70e34dfcb4cd1909413906ed171351021129190', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='uid',
            field=models.CharField(default='5b791913fe704cc589638603c66d5570171351021196030', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='uid',
            field=models.CharField(default='57c1c05b587c4f6ca41a15a142e7fcb5171351021135183', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='uid',
            field=models.CharField(default='31f1fba0000d45219bfd4f2a613dc3e0171351021192025', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productordertodeliverystatus',
            name='uid',
            field=models.CharField(default='7c44a36742df446d94f1f89f3b2a93cb171351021119575', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='7ae97a600fee4ef58c49304308355dde171351021150516', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.CharField(default='1fa77f4dc2d740b2974f418e5e1bb99e171351021196027', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='uid',
            field=models.CharField(default='d11a0263fe9c46a7bd1ffddfcb54ed3c171351021195541', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ProductVarient',
            fields=[
                ('uid', models.CharField(default='7c6db94f80a244068213aa4e97411cbf171351021130261', max_length=255, primary_key=True, serialize=False)),
                ('varient_value', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_varient', to='apps.product')),
                ('product_discount', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='discount', to='apps.productdiscount')),
                ('product_inventory', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory', to='apps.productinventory')),
                ('varient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_varient', to='apps.productcategoryvarient')),
            ],
        ),
        migrations.AddField(
            model_name='productcategoryvarient',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_variants', to='apps.productcategory'),
        ),
        migrations.AlterField(
            model_name='productattachment',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='product_attachment', to='apps.productvarient'),
        ),
    ]