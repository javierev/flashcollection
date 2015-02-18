from django.db import models

class Type(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return 'Type: ' + self.name

class CollectibleDefinition(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)

	def __str__(self):
		return 'Collectible definition: ' + self.name

class PropertyDefinition(models.Model):
	key_name = models.CharField(max_length=50)
	property_type = models.ForeignKey(Type)
	collectible_definition = models.ForeignKey(CollectibleDefinition)
	value_size = models.IntegerField(default=10)

	def __str__(self):
		return 'Property Definition: ' + self.key_name

class Collectible(models.Model):
	collectible_definition = models.ForeignKey(CollectibleDefinition)

	def __str__(self):
		return 'Collectible with ' + self.collectible_definition

class Property(models.Model):
	collectible = models.ForeignKey(Collectible)
	property_definition = models.ForeignKey(PropertyDefinition)
	value = models.CharField(max_length=5000)

	def __str__(self):
		return 'Property with ' + self.property_definition + ' and value ' + self.value