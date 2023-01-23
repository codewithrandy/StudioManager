from django.db import models

class Customer(models.Model):

    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note = models.TextField()


    def __str__(self):
        return self.name


    # JSON
    def get_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'target': self.target,
            'revenue': self.revenue,
            'gender': self.gender,
        }