from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
import api.v1.book as bookapi

port = 4000

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


def test(a,b):
    return a+b


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}

    #if request.path == '/api/v1':

    dispatcher["getbooklist"] = bookapi.bookinfo
    dispatcher["getbooklist"] = bookapi.booklist
    dispatcher["makebook"] = bookapi.makebook
    dispatcher["removebook"] = bookapi.removebook

    dispatcher["instinfo"] = bookapi.instinfo
    dispatcher["bookinginst"] = bookapi.bookinginst
    dispatcher["removeinst"] = bookapi.removeinst
    dispatcher["moveinst"] = bookapi.moveinst

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


def run():
    run_simple('localhost', port, application )


if __name__ == '__main__':
    print ('start')
    run_simple('localhost', port, application, )