'''
Created on Oct 8, 2014

@author: kylegoetz
'''

from peewee import Model, ForeignKeyField, DateTimeField, TextField, IntegerField, Proxy
from decimal import Decimal as D

def add_entry(latitude, longitude, altitude, provider, accuracy, time):
	if GPS_Provider.select().where(GPS_Provider.name == provider).count() == 0:
		provider = GPS_Provider.create(name = provider)
	else:
		provider = GPS_Provider.select().where(GPS_Provider.name == provider)
	GPS_Entry.create(latitude=int(D(latitude)*10**8), longitude=int(D(longitude)*10**8), altitude = int(D(altitude)*10), provider = provider, accuracy = int(D(accuracy)*10), time = time)

dbProxy = Proxy()

class GPS_Provider(Model):
	name = TextField()
	class Meta:
		database = dbProxy

class GPS_Entry(Model):
	'''Note: This will always store time according to UTC zone'''
	altitude = IntegerField() # * 10
	time = DateTimeField(formats=['%Y-%m-%dT%H:%M:%SZ'])
	latitude = IntegerField() # * 1e8
	longitude = IntegerField() # * 1e8
	provider = ForeignKeyField(GPS_Provider)
	accuracy = IntegerField() # * 10

	class Meta:
		database = dbProxy