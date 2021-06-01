from django.db import models


class cliente(models.Model):
	ccod = models.AutoField(primary_key=True)
	cfechac = models.DateField()
	cnombre = models.CharField(max_length=25)
	cnfiscal = models.IntegerField(unique = True)
	cdcfiscal = models.CharField(max_length=35)
	cdcdespacho = models.CharField(max_length=30)
	climite = models.IntegerField()

	def __str__(self):
		return self.cnombre
