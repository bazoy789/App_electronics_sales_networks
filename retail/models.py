from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=150)
    arrears = models.FloatField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Contacts(models.Model):
    email = models.EmailField(max_length=50)
    country = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    street = models.TextField(max_length=50)
    number_house = models.TextField(max_length=10)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Products(models.Model):
    title = models.TextField(max_length=100)
    model = models.TextField(max_length=100)
    create_up_market = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Factory(BaseModel):
    supplier = models.CharField(max_length=150, null=True, blank=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailNetwork(BaseModel):
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IndividualEntrepreneur(BaseModel):
    supplier = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
