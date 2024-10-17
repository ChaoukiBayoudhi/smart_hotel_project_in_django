from django.db import models

# Create your models here.
class Address(models.Model):
    streetName=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    ZipCode=models.CharField(max_length=5)
    
class Hotel(models.Model):
    #id=models.IntegerField(primary_key=True)
    #id=models.AutoField()
    name=models.CharField(max_length=100,unique=True,null=False,blank=False)
    capacity=models.PositiveSmallIntegerField(default=100)
    #nbStars=models.PositiveSmallIntegerField(default=0)
    nbStars=models.CharField(max_length=2,choices=[('3','Three Stars'),('4','Four Stars'),('5','Five Stars')])
    #implementing the relationship between Hotel and Address (1-1)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True,blank=True)
#Enumeration type
class RoomType(models.TextChoices):
    standard=('STD','standard')
    deluxe=('DLX','deluxe')
    suite=('STE', 'suite')
    other=('OTH','other')

class Room(models.Model):
    number=models.PositiveIntegerField(primary_key=True)
    type=models.CharField(max_length=10,choices=RoomType.choices,default=RoomType.standard)
    rate=models.DecimalField(max_digits=2,decimal_places=1)
    #relationship between room and Hotel(n-1)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True, blank=True)
    status=models.BooleanField(default=True)

class Guest(models.Model):
    cin=models.CharField(max_length=8,null=True,blank=True,)#validators=[MinLengthValue=8])
    passportNumber=models.CharField(max_length=12,null=True,blank=True)
    name=models.CharField(max_length=100)
    familyName=models.CharField(max_length=100)
    nationality=models.CharField(max_length=50)
    #implement the relationship between Guest and Room (*-*) through Reservation
    reservations=models.ManyToManyField(Room,through='Reservation',through_fields=('guest','room'))

    def clean(self):
        if self.cin is None and self.passportNumber is None:
            raise ValueError('cin or passport number is required.')

class Reservation(models.Model):
    guest=models.ForeignKey(Guest, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    reservationDate=models.DateTimeField(auto_now_add=True)
    inDate=models.DateTimeField(auto_now_add=True)
    outDate=models.DateTimeField(auto_now_add=True)
    totalAmount=models.DecimalField(max_digits=7, decimal_places=2)
    status =models.CharField(max_length=20,choices=[('active','active'),('cancelled','cancelled')])
    class Meta:
        unique_together =['room','guest']
        ordering = ['inDate'] #ASC order
        #ordering = ['-inDate] #DES order
        
