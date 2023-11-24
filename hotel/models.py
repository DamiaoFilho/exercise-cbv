from django.db import models

# Create your models here.



class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(max_length=100, verbose_name="Telefone")
    address = models.CharField(max_length=100, verbose_name="Endereço")

class Reserve(models.Model):
    date_entry = models.DateField(verbose_name="Data de entrada")
    date_out = models.DateField(verbose_name="Data de saída")
    value = models.FloatField(verbose_name="Valor")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    room = models.ForeignKey("Room", on_delete=models.CASCADE, verbose_name="Quarto")

class Consume(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    date = models.DateField(verbose_name="Data")
    value = models.FloatField(verbose_name="Valor")
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE, verbose_name="Hospedagem")

class Room(models.Model):
    apartment = models.IntegerField(verbose_name="Apartamento")
    value = models.FloatField(verbose_name="Valor")


