'''
Created on Oct 8, 2014

@author: kylegoetz
'''
import cherrypy
import Db
from com.kylegoetz.lib import template
import json

class GPSServer(object):
	__TEMPLATE_PATH = '/templates/'
	__PACKAGE_PATH = 'gps/'
	
	@cherrypy.expose
	def log_gps(self, **params):
		print(params)
		print(params['time'][1])
		Db.add_entry(params['latitude'],
				params['longitude'],
				params['altitude'],
				params['provider'],
				params['accuracy'],
				#params['time'].split("u'")[-1][:-2])
				params['time'][1])
	
	@cherrypy.expose
	@template.output(__TEMPLATE_PATH+__PACKAGE_PATH+'plot.html')
	def gps_map(self):
		return template.render()
		
	@cherrypy.expose
	def get_gps(self, **params):
		locations = [{'latitude':location.latitude/100000000.0,'longitude':location.longitude/100000000.0, 'provider':location.provider.name} for location in Db.GPS_Entry.select().where(Db.GPS_Entry.provider==2).limit(int(params['numberOfPoints']))]
		return json.dumps({'locations':locations})
	
	@cherrypy.expose
	@template.output(__TEMPLATE_PATH+__PACKAGE_PATH+'delta.html')
	def plot_del(self):
		locations = [{'latitude':location.latitude/100000000.0,'longitude':location.longitude/100000000.0, 'time':location.time.isoformat()} for location in Db.GPS_Entry.select().where(Db.GPS_Entry.provider==2).limit(10)]
		#note to convert date in Javascript, jsut have to do new Date(date)
		return json.dumps({'locations':locations})
	
	@cherrypy.expose
	def get_current_location(self):
		result = (Db.GPS_Entry.select().order_by(Db.GPS_Entry.time.desc()).get())
		return json.dumps({'latitude':result.latitude/100000000.0, 'longitude':result.longitude/100000000.0})
	
	@cherrypy.expose
	@template.output(__TEMPLATE_PATH+__PACKAGE_PATH+'current_location.html')
	def current_location(self):
		return template.render()