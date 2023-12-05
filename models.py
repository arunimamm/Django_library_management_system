from django.db import models

# Create your models here.
class book_management(models.Model):
    title = models.CharField(max_length = 30)
    genere = models.CharField(max_length = 30)
    ISBN = models.CharField(max_length = 20)
    avalability = models.BooleanField

    def __str__(self):
        return self.title

class patron_management(models.Model):
    library_no = models.AutoField
    name = models.CharField(max_length = 30)
    contact = models.CharField(max_length = 30)
    member_detail = models.CharField(max_length = 20)

    def __str__(self):
        return self.library_no
    
class book_borrowing(models.Model):
    book = models.CharField(max_length = 30)
    patron = models.CharField(max_length = 30)
    borrowing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.borrowing_date


