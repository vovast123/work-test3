from tabnanny import verbose
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User 
from src.base.services import get_path_upload_product_image, validate_size_image,get_path_upload_profile_image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        default='no-avatar.jpeg',
        upload_to=get_path_upload_profile_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_size_image],
    )
    for_checking = models.BooleanField('Checking',default=False)
    code = models.TextField('Code company',blank=True)
    check_code = models.BooleanField('Check',default=False)
    check_code_fail = models.BooleanField('Fail',default=False)
    date_created = models.DateTimeField('Time from check_code aplly ',default=timezone.now)
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
    category_sub = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE,
        related_name='product_category_sub', verbose_name="Category of product"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")
    phone = models.SmallIntegerField('phone number',default=0,blank=True)
    contact = models.TextField(max_length=1000, verbose_name="contact information")
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


    def __str__(self):
        return f"{self.owner} - {self.title}"

    class Meta:
        ordering = ("title", )
        index_together = (("id", "slug"), )
        verbose_name = "Product"
        verbose_name_plural = "Products"






class ProductComment(models.Model):
    """ Модель комментарий к товару """


    RATING_CHOICE = (
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_comments",
        verbose_name="Комментарий к товару"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="comment_author",
        verbose_name="Автор комментария"
    )

    rating = models.CharField(
        max_length=2, choices=RATING_CHOICE,
        default="0", verbose_name="Рейтинг"
    )

    text = models.TextField(
        max_length=2000, verbose_name='Текст комментария'
    )
    is_valid = models.BooleanField(
        default=True, verbose_name="Валидный"
    )
    date_created = models.DateTimeField('Time',default=timezone.now)

    class Meta:
        ordering = ("date_created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author} - {self.product}"



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


class SubCategoryLegal(models.Model):
    """ Модель подкатегорий """
    category = models.ForeignKey(
        CategoryLegal, on_delete=models.CASCADE,
        related_name="sub_categorylg", verbose_name="Category"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")

    def __str__(self):
        return f"{self.category} ({self.title})"

    class Meta:
        ordering = ("title", )
        verbose_name = "SubCategoryLegal"
        verbose_name_plural = "SubCategoryLegals"



class LegalProduct(models.Model):
    owner = models.ForeignKey(
        User, related_name="product_owner_lg",
        on_delete=models.CASCADE, verbose_name="owner"
    )
    category_sub = models.ForeignKey(
        SubCategoryLegal, on_delete=models.CASCADE,
        related_name='product_category_sub_lg', verbose_name="Category of product"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="title")
    slug = models.SlugField(unique=True, verbose_name="Link")
    phone = models.SmallIntegerField('phone number',default=0)
    contact = models.TextField(max_length=1000,blank=True,null=True ,verbose_name="contact information")
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

    def __str__(self):
        return f"{self.owner} - {self.title}"

    class Meta:
        ordering = ("title", )
        index_together = (("id", "slug"), )
        verbose_name = "Legal product"
        verbose_name_plural = "Legal products"

        
class ProductCommentLg(models.Model):
    """ Модель комментарий к товару """


    RATING_CHOICE = (
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )

    product = models.ForeignKey(
        LegalProduct, on_delete=models.CASCADE,
        related_name="product_comments_lg",
        verbose_name="Комментарий к товару"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="comment_author_lg",
        verbose_name="Автор комментария"
    )

    rating = models.CharField(
        max_length=2, choices=RATING_CHOICE,
        default="0", verbose_name="Рейтинг"
    )

    text = models.TextField(
        max_length=2000, verbose_name='Текст комментария'
    )
    is_valid = models.BooleanField(
        default=True, verbose_name="Валидный"
    )
    date_created = models.DateTimeField('Time',default=timezone.now)

    class Meta:
        ordering = ("date_created",)
        verbose_name = "Комментарий юр у"
        verbose_name_plural = "Комментарии юр у"

    def __str__(self):
        return f"{self.author} - {self.product}"