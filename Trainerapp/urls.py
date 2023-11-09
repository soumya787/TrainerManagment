from django.urls import path

from Trainerapp import views

urlpatterns=[
    path('register',views.reg_fun,name='register'), #it will display register.html
    path('regdata',views.reg_data_fun), #it will store the data either in User table or in reg table

    path('',views.log_fun,name='log'), #it will display login.html
    path('logread',views.log_read_fun), #it will

    path('Ahome', views.admin_home_fun, name='Ahome'), #display Admin homepage
    
    path('trainer_details',views.trainer_details, name='trainer_details'),# it will display all the trainer details
    
    path('batch_Assign', views.batch_data_fun,name='batch_Assign'),  # it will redirect to batchassign.html page
    path('readdata',views.batch_assign_fun), # it will store all the data inside Trainer_Batch_assign table

    path('batchdetails',views.batch_details, name='batchdetails'),    
    path('delete/<int:x>',views.delete_fun,name='delete'),#it will particular trainer details
    path('update/<int:id>',views.update_fun,name='update'), # it will update the trainer batch assigned details
    
    path('log_out',views.logout_fun,name='log_out'),

    path('Thome', views.trainer_home_fun, name='Thome'), #it will display Trainer Homepage
    path('trainerdata',views.trainer_data_fun,name='trainerdata')
]