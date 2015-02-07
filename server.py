import os, cherrypy

from com.kylegoetz.GPS.Server import GPSServer

class Server(GPSServer, object):
	
	@cherrypy.expose
	def index(self):
		return "Hello World"

conf = {
	'/' : {
		'tools.sessions.on': True,
		'tools.staticdir.root': os.path.abspath(os.getcwd()) 
	},
	'/public': {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': './public'
	}
}
cherrypy.quickstart(Server(), '/', conf)