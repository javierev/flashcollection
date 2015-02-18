#  Flash Collection - modular collection database
#    Copyright (C) 2015  Javier Estevez (jestevez at valdaris.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
