from django.db import models


class Category(models.Model):
    category=models.CharField(max_length=50)


    def __str__(self):
        return self.category


class Nationality(models.Model):
    nationality=models.CharField(max_length=50)


    def __str__(self):
        return self.nationality


class Players(models.Model):
    ismi=models.CharField(max_length=50)
    jinsi=models.CharField(max_length=50)
    sport_turi=models.ForeignKey(Category,on_delete=models.CASCADE)
    millati=models.ForeignKey(Nationality,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.ismi},{self.jinsi}"





