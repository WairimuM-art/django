from django.contrib import admin

from .models import Students

from .models import Contact

from .models import Employees

from .models import Login
# from .views import login_registration
# from .templates:('login_registration') import Login


# Register your models here.
admin.site.register(Students)
admin.site.register(Contact)
admin.site.register(Employees)
admin.site.register(Login)
