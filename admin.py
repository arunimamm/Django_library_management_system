from django.contrib import admin

# Register your models here.
from lms.models import book_management,patron_management,book_borrowing

admin.site.register(book_management)
admin.site.register(patron_management)
admin.site.register(book_borrowing)
