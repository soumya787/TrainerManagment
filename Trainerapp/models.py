from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}'


class City(models.Model):
    city_name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city_name}'


class Trainer_Reg(models.Model):
    Tname=models.CharField(max_length=50)
    Tage=models.CharField(max_length=50)
    TPhno=models.BigIntegerField()
    Temail=models.EmailField(max_length=50)
    Tpassword=models.CharField(max_length=50)
    Tcity=models.ForeignKey(City,on_delete=models.CASCADE)
    Tcourse=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Tname}'

class Trainer_Batch_Assign(models.Model):
    Tr_name=models.ForeignKey(Trainer_Reg,on_delete=models.CASCADE)
    BatchNo=models.IntegerField()
    Date=models.DateTimeField()
    Tr_Course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Date},{self.BatchNo}'