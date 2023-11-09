from django.contrib import admin

# Register your models here.


from Trainerapp.models import Course, Trainer_Batch_Assign, Trainer_Reg, City

admin.site.register(Course)
admin.site.register(City)
admin.site.register(Trainer_Reg)
admin.site.register(Trainer_Batch_Assign)


