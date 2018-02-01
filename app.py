import cherrypy
import os
import requests, json
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('html'))
#todo: change favicon?
#      get data from form and send it to functions

register_page = "http://52.233.158.172/change/api/en/account/register"
login_page = "http://52.233.158.172/change/api/hr/account/login"
details_page = "http://52.233.158.172/change/api/hr/team/details/"
confirm_page = "http://52.233.158.172/change/api/hr/team/confirm"

class IndexPage(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

class RegisterPage(object):
    @cherrypy.expose
    def register():
        print "implement me."

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('register.html')
        return tmpl.render()

class DisplayPage(object):
    @cherrypy.expose
    def confirmDetails():
        print "implement me."

    @cherrypy.expose
    def listDetails():
        print "implement me."

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('display.html')
        return tmpl.render()

class LoginPage(object):
    @cherrypy.expose
    def login():
        print "implement me."

    @cherrypy.expose
    def index(self):
        out_dat = ''
        tmpl = env.get_template('login.html')
        return tmpl.render(data=out_dat)

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

cherrypy.tree.mount(RegisterPage(), '/register', config=config)
cherrypy.tree.mount(DisplayPage(), '/display', config=config)
cherrypy.tree.mount(LoginPage(), '/login', config=config)
cherrypy.quickstart(IndexPage(), '/', config=config)