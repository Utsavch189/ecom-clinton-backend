from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password,check_password
import random
from utils.id_generate.main import generate_id

class UserRole(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    role_name=models.CharField(max_length=30,unique=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.role_name=self.role_name.upper()
        super(UserRole, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.role_name

class User(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True,db_index=True)
    password=models.TextField()
    phone=models.CharField(max_length=15,db_index=True)
    role=models.ForeignKey(UserRole,on_delete=models.DO_NOTHING,related_name='roles')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.email=self.email.lower()
        self.password=make_password(self.password)
        super(User, self).save(*args, **kwargs)
    
    def is_correct_password(self,password:str):
        if check_password(password,self.password):
            return True
        return False
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class UserAddress(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users_address',default="")
    address_line1=models.CharField(max_length=255)
    address_line2=models.CharField(max_length=255, null=True,blank=True)
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return f"Address of {self.user.first_name} {self.user.last_name}"

class ProductCategory(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    category_name=models.CharField(max_length=255,db_index=True)
    image=models.FileField(null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,default="",null=True,blank=True,related_name="category_user")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.category_name=self.category_name.upper()
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

class ProductBrand(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    brand_name=models.CharField(max_length=255,db_index=True)
    image=models.FileField(null=True,blank=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='brand_category',default="")
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,default="",null=True,blank=True,related_name="brand_user")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.brand_name=self.brand_name.upper()
        super(ProductBrand, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.brand_name
    
class VariantOptions(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    varient_name=models.CharField(max_length=255)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='category_variants')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.varient_name=self.varient_name.upper()
        super(VariantOptions, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"varient : {self.varient_name} category : {self.category.category_name}"

class ProductInventory(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    quantity=models.PositiveIntegerField()
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,default="",null=True,blank=True,related_name="inventory_user")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return self.uid

class ProductDiscount(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    discount_name=models.CharField(max_length=255)
    discount_desc=models.TextField()
    discount_percentage=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,default="",null=True,blank=True,related_name="discount_user")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.discount_name=self.discount_name.upper()
        super(ProductDiscount, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.discount_name


class Product(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    product_name=models.CharField(max_length=100)
    product_brand=models.ForeignKey(ProductBrand,on_delete=models.CASCADE,related_name='brand',default="")
    product_category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="category",default="")
    product_desc=models.TextField(null=True,blank=True)
    product_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    product_discount=models.ForeignKey(ProductDiscount,on_delete=models.SET_DEFAULT,related_name="product_discount",default="",null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,default="",null=True,blank=True,related_name="product_user")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    @property
    def get_price(self):
        if not self.product_discount.discount_percentage:
            return self.product_price
        return self.product_price-(self.product_price*self.product_discount.discount_percentage/100)


    def save(self, *args, **kwargs):
        self.product_name=self.product_name.upper()
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

class ProductVarient(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    desc=models.TextField(null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_varient')
    product_inventory=models.ForeignKey(ProductInventory,on_delete=models.SET_DEFAULT,related_name="inventory",default="")
    varient_discount=models.ForeignKey(ProductDiscount,on_delete=models.SET_DEFAULT,related_name="varient_discount",default="",null=True,blank=True)
    product_price_adjustment=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return f"product : {self.product.product_name} "

class VarientAttribute(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    varient=models.ForeignKey(ProductVarient,on_delete=models.CASCADE,related_name='product_varient')
    options=models.ForeignKey(VariantOptions,on_delete=models.CASCADE,related_name='varient_options')
    value=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs) -> None:
        self.value=self.value.upper()
        super(VarientAttribute, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.uid)


class ProductAttachment(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    attachment_id=models.CharField(max_length=100,unique=True,db_index=True)
    file_type=models.CharField(max_length=100)
    file=models.FileField()
    caption=models.CharField(max_length=255,null=True,blank=True)
    product=models.ForeignKey(ProductVarient,on_delete=models.CASCADE,related_name='product_attachment',default="")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return self.attachment_id

class CartItem(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_carts",default="")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_carts",default="")
    cart_quantity=models.PositiveIntegerField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.uid=str(self.uid)+str(int(datetime.timestamp(datetime.now())))+str(random.randint(1111,9999))
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Cart of {self.user.first_name} {self.user.last_name} for {self.product.product_name}"

class ProductOrderToDeliveryStatus(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    step_name=models.CharField(max_length=255,unique=True,db_index=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(default=None,null=True,blank=True)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.step_name=self.step_name.upper()
        super(ProductOrderToDeliveryStatus, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.step_name

class Payment(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    transaction_id=models.CharField(max_length=100,unique=True,db_index=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='user_payment')
    razorpay_order_id=models.CharField(max_length=100)
    razorpay_payment_id=models.CharField(max_length=100)
    razorpay_signature=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return self.transaction_id

class Invoice(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    invoice_id=models.CharField(max_length=100,unique=True,db_index=True)
    invoice=models.CharField(max_length=255)
    invoice_for=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='user_invoice')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return self.invoice_id


class Order(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    order_id=models.CharField(max_length=100,unique=True,db_index=True)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_orders",default="")
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name="product_orders",default="")
    order_payment=models.ForeignKey(Payment,on_delete=models.DO_NOTHING,related_name="payment_order",default="")
    order_status=models.ForeignKey(ProductOrderToDeliveryStatus,on_delete=models.DO_NOTHING,related_name="status_order",default="")
    order_invoice=models.ForeignKey(Invoice,on_delete=models.DO_NOTHING,related_name='invoice_order',default="")
    order_quantity=models.PositiveIntegerField()
    order_total_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_accepted_by_customer=models.BooleanField(default=False)
    is_invoice_send=models.BooleanField(default=False)
    invoice_sent_at=models.DateTimeField(default=None)
    otp_for_verify=models.CharField(max_length=6)
    otp_expiry=models.DateTimeField(default=None)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return self.order_id

class ErrorLog(models.Model):
    uid = models.CharField(max_length=255, default=generate_id(), primary_key=True)
    error_message=models.TextField()
    user_id=models.CharField(max_length=255,null=True,blank=True)
    user_type=models.CharField(max_length=255,null=True,blank=True)
    request_method=models.CharField(max_length=255,null=True,blank=True)
    request_headers=models.TextField(null=True,blank=True)
    request_parameters=models.CharField(max_length=255,null=True,blank=True)
    request_body=models.TextField(null=True,blank=True)
    client_ip=models.CharField(max_length=255,null=True,blank=True)
    stack_trace=models.TextField()
    exception_type=models.CharField(max_length=255,null=True,blank=True)
    view_name=models.CharField(max_length=255,null=True,blank=True)
    response_status_code=models.CharField(max_length=255,null=True,blank=True)
    enviroment=models.CharField(max_length=255,null=True,blank=True)
    error_location=models.CharField(max_length=255,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f"Error : {self.response_status_code} at {self.created_at}"

class AccessLog(models.Model):
    uid = models.CharField(max_length=100, default=generate_id(), primary_key=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    request_method = models.CharField(max_length=255, null=True, blank=True)
    request_headers = models.TextField(null=True, blank=True)
    request_parameters = models.CharField(max_length=255, null=True, blank=True)
    request_body = models.TextField(null=True, blank=True)
    client_ip = models.CharField(max_length=255, null=True, blank=True)
    view_name = models.CharField(max_length=255, null=True, blank=True)
    response_status_code = models.CharField(max_length=255, null=True, blank=True)
    environment = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    response_content = models.TextField(null=True, blank=True)
    request_url = models.URLField(max_length=2000, null=True, blank=True)
    user_agent = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    referer = models.URLField(max_length=2000, null=True, blank=True)
    request_query_params = models.JSONField(null=True, blank=True)
    response_headers = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Log: {self.response_status_code} at {self.created_at} method {self.request_method} url {self.request_url}"
