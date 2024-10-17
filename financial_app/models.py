from django.db import models

from hotel_app.models import Room,Reservation

# Create your models here.
class Expense(models.Model):
    category = models.CharField(max_length=10,choices=[('SAL','Salaries') ,('UTL','utilities'),('MTN','maintenance')])
    amount=models.FloatField()
    date=models.DateField(auto_now_add=True)
    description=models.TextField()
    #implement the relationship between Expense and Room (*-*)
    room_expense=models.ManyToManyField(Room)

    def __str__(self):
        return f'category : {self.category}, date : {self.date}, amount: {self.amount}'

class PaymentMethod(models.TextChoices):
    CASH=('CASH','Cash payment')
    CREDIT_CARD=('CARD','Credit card payment')
    CHECK=('CHECK','Check payment')

class Payment(models.Model):
    method=models.CharField(max_length=5,choices=PaymentMethod.choices,default=PaymentMethod.CASH)
    reservation=models.ForeignKey(Reservation,on_delete=models.SET_NULL, null=True)
    date=models.DateField(auto_now_add=True)
    amount=models.DecimalField(max_digits=9,decimal_places=2)
    def __str__(self):
        return f'reservation: {self.reservation.id}, method: {self.method}, date: {self.date}'