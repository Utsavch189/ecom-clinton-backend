# Generated by Django 4.2 on 2024-04-20 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_alter_accesslog_uid_alter_cartitem_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='uid',
            field=models.CharField(default='7a099c526ad145a2816637a2ec8e3a6f171362182886235', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='uid',
            field=models.CharField(default='f2433249259c47a89d69baf117e60e64171362182863351', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='uid',
            field=models.CharField(default='42d046a02bb949e6a2488ad56ce53071171362182863867', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_invoice', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uid',
            field=models.CharField(default='c2109332432145899e8943d58b4ef143171362182843977', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='7e23ecc0d89f448081492fc80f65a870171362182862351', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='uid',
            field=models.CharField(default='a2f9e9fe05194e65ba2241d812dc1695171362182897393', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_payment', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_user', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(default='3fe5c30711eb4f93bb878daf828fc3c8171362182821818', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productattachment',
            name='uid',
            field=models.CharField(default='a4002873bd794b689405e098f5d5f096171362182877287', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_user', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='uid',
            field=models.CharField(default='cf9b2145fc424bb9af9af96941b6770a171362182877568', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_user', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='uid',
            field=models.CharField(default='cee1cc05c8834ed3ba8dd5a8355fe40c171362182886412', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discount_user', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='uid',
            field=models.CharField(default='c1fb3c839b6949ce974d110dcc3c9ceb171362182832314', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory_user', to='apps.user'),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='uid',
            field=models.CharField(default='5c50a4819066403292c2db0a2da007e4171362182846768', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productordertodeliverystatus',
            name='uid',
            field=models.CharField(default='aa00137ca8044c1cb0e75c19447c12ac171362182836704', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productvarient',
            name='uid',
            field=models.CharField(default='192b290896dc4d62897842fc04a2172a171362182888292', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='344beeffeb604f58951609f420a6f204171362182859760', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.CharField(default='b743209b8a4845d8a961bf7376d037e5171362182855951', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='uid',
            field=models.CharField(default='bd84c7dd97e14e8cb8f7f6e0a5b56ede171362182843527', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='variantoptions',
            name='uid',
            field=models.CharField(default='cfcfda6db910488cafa9dca4c2ece114171362182846082', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='varientattribute',
            name='uid',
            field=models.CharField(default='8f6364667fcd4fb38bad92bed0ce4a71171362182889961', max_length=255, primary_key=True, serialize=False),
        ),
    ]
