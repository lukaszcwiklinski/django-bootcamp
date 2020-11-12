from django.db import models

# Create your models here.


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Software', 'SOFTWARE'),
        ('Fintech', 'FINTECH'),
        ('Outsourcing', 'OUTSOURCING'),
    ]
    name = models.CharField(verbose_name='Nazwa kategorii', choices=CATEGORY_CHOICES, max_length=100)

    class Meta:
        verbose_name_plural = 'Kategorie'

    def __repr__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    post_code = models.IntegerField(default='11111')

    class Meta:
        verbose_name_plural = 'Adresy'

    def __str__(self):
        return self.street


class Company(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=60, null=False)
    registration_date = models.DateField(verbose_name='Rejestracja')
    owner = models.CharField(verbose_name='Właściciel', max_length=60)
    description = models.TextField(verbose_name='Opis')
    category = models.ForeignKey(Category, verbose_name='Kategoria', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email')
    address = models.ManyToManyField(Address, verbose_name='Adres')
    created_at = models.DateField(verbose_name='Data utworzenia', auto_now_add=True)
    phone_number = models.CharField(verbose_name='Telefon', max_length=60)
    is_active = models.BooleanField(verbose_name='Aktywna', default=True)

    class Meta:
        verbose_name_plural = 'Firmy'

    def __str__(self):
        return self.name
