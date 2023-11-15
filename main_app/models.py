from django.db import models
from django.urls import reverse
from datetime import date

# data
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    where_to_find = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("single_finch", kwargs={"finch_id": self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS) #returns true if condition met

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"