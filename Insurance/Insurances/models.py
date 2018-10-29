from django.db import models
from random import randint
# Create your models here.
from django.db import models
class Customer(object):
    customer_id = 101
    customer_name = "Niraj"
    saving_acc_no = 123456789
    account_balance = 100000

def get_random_id():
    return randint(10000,99999)

class Insurance(models.Model):
    My_choices =(('h', 'home'),
                 ('v','vehical'),
                 ('p', 'personal'))
    My_choices_1 = (( 'a','one Lakh'),
                 ('b','5 Lakh'),
                 ('c','10lakh'))
    insu_id = models.AutoField(primary_key=True)
    cust_id = models.IntegerField(default=Customer.customer_id)
    insu_acc_no = models.IntegerField(default=get_random_id, unique=True)
    insurance_type = models.CharField(max_length= 100 ,choices= My_choices)
    total_insurance = models.CharField(max_length= 200,choices= My_choices_1)
    object = models.Manager()

    def __str__(self):
        return str(self.insu_id)

class Transacts(models.Model):
    My_choices_1 = (('a', 'one Lakh'),
                    ('b', '5 Lakh'),
                    ('c', '10lakh'))
    trans_id = models.AutoField(primary_key=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='transactions')
    cust_id = models.IntegerField(default=Customer.customer_id)
    Insurance_accnt = models.CharField(choices=My_choices_1,max_length=100)



