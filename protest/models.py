from django.db import models
from django.core.validators import MinValueValidator



# Create your models here.


class Protest(models.Model) :
    TYPE_CHOICES = (
        ('a', '집회'), #a,b,c,d,e는 꼭 있어야하는가?
        ('b', '서명운동'),
        ('c', '전시'),
        ('d', '플래시몹'),
        ('e', '모금'),
        ('f', '기타'),
    )
    type_of = models.CharField(max_length=50, choices = TYPE_CHOICES, default='a')
    title = models.CharField(max_length=100)
    content = models.TextField(blank = True)
    photo = models.ImageField(blank=True)
    video = models.URLField(blank=True)
    place = models.TextField(blank=True)
    date = models.DateField(blank=True)
    number_of_people = models. PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ])
    user = models.ForeignKey('User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class User(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=200)

    def __str__(self) :
        return self.nickname



class Participation(models.Model):
    protest = models.ForeignKey(Protest)
    user = models.ForeignKey(User)


class Donation(models.Model):
    protest = models.ForeignKey(Protest)
    amount = models.PositiveIntegerField(default=1000)
    account_number = models.PositiveIntegerField(default=1)
    BANK_CHOICES = (
        ('a', '신한은행'), #a,b,c,d,e는 꼭 있어야하는가?
        ('b', '국민은행'),
        ('c', '하나은행'),
        ('d', '기업은행'),
        ('e', '농협은행'),
    )
    bank = models.CharField(max_length=50, choices = BANK_CHOICES, default='a')


class DonationState(models.Model):
    protest = models.ForeignKey(Protest)
    user = models.ForeignKey(User)
