from django.db import models

class Offers(models.Model):
    Regular = 0
    Valentine = 1
    Diwali = 2
    Christmas = 3
    NYE = 4
    Others =5
    Type_Offer = (
        (Regular, 'Regular'),
        (Valentine, 'Valentine'),
        (Diwali, 'Diwali'),
        (Christmas, 'Christmas'),
        (NYE, 'New_Year_Eve'),
        (Others, 'Others'),
    )
    offer = models.SmallIntegerField(choices=Type_Offer, default=Regular)
    offer_perc = models.PositiveIntegerField(default=0)
    offer_tnc = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.offer) + "," + str(self.offer_perc)

class Menu(models.Model):
    Starters = 0
    Mocktail = 1
    Lunch = 2
    Dinner = 3
    Type_Menu = (
        (Starters, 'Starters'),
        (Mocktail, 'Mocktail'),
        (Lunch, 'Lunch'),
        (Dinner, 'Dinner')
    )

    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_INACTIVE, 'Inactive'),
        (STATUS_ACTIVE, 'Active')
    )
    menu = models.SmallIntegerField(choices=Type_Menu, default=None)
    dish_name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    offers_avail = models.ForeignKey(Offers, on_delete = models.CASCADE)
    combo_avail = models.SmallIntegerField(choices = STATUS_CHOICES, default=STATUS_ACTIVE)
    image_url = models.CharField(max_length=200, blank=True, default="")
    dish_status =models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    def __str__(self):
        return str(self.dish_name) + "," + str(self.menu)

class Combo(models.Model):
    dish1 = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='dish1', unique=True)
    dish2 = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='dish2', unique=True,blank=True, null=True)
    dish3 = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='dish3', unique=True,blank=True, null=True)
    dish4 = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='dish4', unique=True,blank=True, null=True)
    dish5 = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='dish5', unique=True,blank=True, null=True)
    def __str__(self):
        return str(self.dish1)

