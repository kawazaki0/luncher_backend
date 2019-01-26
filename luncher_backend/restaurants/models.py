from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    street_number = models.IntegerField(null=True)
    street = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    tel_number = models.CharField(max_length=20, null=True)
    min_purchase = models.IntegerField(default=0)

    @property
    def address(self):
        return '{} {} {} {}'.format(self.street, self.street_number, self.city, self.zip_code)

    def __str__(self):
        return '{} {}'.format(self.name, self.city)

    class Meta:
        db_table = 'restaurant'


class MealCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'meal_category'


class Meal(models.Model):

    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'
    DAYS = (
        (MONDAY,'Monday'),
        (TUESDAY,'Tuesday'),
        (WEDNESDAY,'Wednesday'),
        (THURSDAY,'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY,'Sunday')
    )

    name = models.CharField(max_length=1000)  # string
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.IntegerField()  # TODO decimal or string or money
    date = models.CharField(choices=DAYS,max_length=100)  # TODO date without time
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.restaurant)

    class Meta:
        db_table = 'meal'
