import os
from com.kylegoetz.GPS.Db import GPS_Entry, GPS_Provider, dbProxy
from urllib2 import urlopen
from peewee import SqliteDatabase
from decimal import Decimal as D 

db = SqliteDatabase('./data/gps.sqlite', check_same_thread = False)
dbProxy.initialize(db)

if not os.path.isfile('./data/gps.sqlite'):
	dbProxy.connect()
	dbProxy.create_table(GPS_Provider)
	dbProxy.create_table(GPS_Entry)

def store_data(data):
	ofile = open('./data/gps.log','a')
	ofile.write(data+'\n')
	#try:
	#	GPS_Entry.create()
	#except:
	#	return False
	return True
		

if __name__ == '__main__':
	from pprint import pprint
	pprint(store_data(data='Null'))