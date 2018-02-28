#Stokes, Jeff
#Lab Assignment 4 - CS350
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json

f = open('cve.json', 'r')
db = json.loads(f.read())
f.close()


def home_view(request):
    return Response('In the address bar, type /lookup/ followed by the search term. <br/> If nothing is found, the page will inform the user.')

def lookup_view(request):
    output = ''
    mydict = request.matchdict
    for item in db:
        val = db['query']

        if val in item:
            output.append[item + "<br/>"]

    if output != '':
        return Response(output)
    else:
        return Response("Nothing was found.")

#<br/> used to line break

if __name__ == '__main__':

    #Create an instance of the configurator class
    with Configurator() as config:

        #add_route() registers a new route
        config.add_route('home', '/home')
        config.add_route('lookup', 'lookup/{query}')

        #Register a view callable
        config.add_view(home_view, route_name='home')
        config.add_view(lookup_view, route_name='lookup')

        app = config.make_wsgi_app()

        #Serve the wsgi application on localhost port 8080
        server = make_server('0.0.0.0', 8080, app)

server.serve_forever()