from tabnanny import verbose
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from src.base.services import get_path_upload_product_image, validate_size_image,get_path_upload_profile_image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        default='no-avavtar.jpeg',
        upload_to=get_path_upload_profile_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_size_image],
    )
    code = models.TextField('Code company',blank=True)
    check_code = models.BooleanField('Check',default=False)
    check_code_fail = models.BooleanField('Fail',default=False)
    date_created = models.DateTimeField('Time from check_code aplly ',auto_now_add=True)
    def __str__(self):
        return f"{self.user}"
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    


class Category(models.Model):
    """ Модель категорий """

    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("title", )
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    """ Модель подкатегорий """
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="sub_category", verbose_name="Category"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")

    def __str__(self):
        return f"{self.category} ({self.title})"

    class Meta:
        ordering = ("title", )
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"


class Product(models.Model):
    """ Модель товара """

    owner = models.ForeignKey(
        User, related_name="product_owner",
        on_delete=models.CASCADE, verbose_name="owner"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='product_category', verbose_name="Category of product"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")
    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_size_image],
    )
    description = models.TextField(max_length=8000, verbose_name="description")
    available = models.BooleanField(default=True, verbose_name="Availability in stock")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date create")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price of product")
    discount = models.DecimalField(max_digits=8, decimal_places=2,default=0, verbose_name="discount(in dollars)")

    tags = TaggableManager(verbose_name="tags")

    def __str__(self):
        return f"{self.owner} - {self.title}"

    class Meta:
        ordering = ("title", )
        index_together = (("id", "slug"), )
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    """ Модель для загрузки нескольких изображений для товара """

    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_size_image],
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_images", verbose_name="product-images"
    )

class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Name", max_length=100)
    value_rating = models.PositiveSmallIntegerField("value",default=0)
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(Product,related_name="comment", verbose_name="Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="commentparent", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"



#legal services
class CategoryLegal(models.Model):
    """ Модель категорий """

    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("title", )
        verbose_name = "Category for ls"
        verbose_name_plural = "Categories for ls"






class LegalProduct(models.Model):
    owner = models.ForeignKey(
        User, related_name="product_owner_lg",
        on_delete=models.CASCADE, verbose_name="owner"
    )
    category = models.ForeignKey(
        CategoryLegal, on_delete=models.CASCADE,
        related_name='product_category_lg', verbose_name="Category of product"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")
    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_size_image],
    )
    description = models.TextField(max_length=8000, verbose_name="description")
    description_add = models.TextField(max_length=8000, verbose_name="additional description")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date create")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    discount = models.DecimalField(max_digits=8, decimal_places=2,default=0, verbose_name="discount(in dollars)")

    tags = TaggableManager(verbose_name="tags")

    def __str__(self):
        return f"{self.owner} - {self.title}"

    class Meta:
        ordering = ("title", )
        index_together = (("id", "slug"), )
        verbose_name = "Legal product"
        verbose_name_plural = "Legal products"


class ProductImageLg(models.Model):
    """ Модель для загрузки нескольких изображений для товара """

    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_size_image],
    )
    product = models.ForeignKey(
        LegalProduct, on_delete=models.CASCADE,
        related_name="product_images_lg", verbose_name="product-images"
    )

class ReviewsLg(models.Model):
    """Отзывы"""
    name = models.CharField("Name", max_length=100)
    value_rating = models.PositiveSmallIntegerField("value",default=0)
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent_lg", on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(LegalProduct,related_name="comment_lg", verbose_name="Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="commentparent_lg", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Review ls"
        verbose_name_plural = "Reviews ls"