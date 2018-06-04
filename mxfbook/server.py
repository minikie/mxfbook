from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
import api

port = 4000

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


def test(a,b):
    return a+b


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b
    dispatcher["test"] = test

    dispatcher["booklist"] = api.booklist
    dispatcher["bookinfo"] = api.bookinfo
    dispatcher["instinfo"] = api.instinfo


    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


def run():
    run_simple('localhost', port, application )


if __name__ == '__main__':
    run_simple('localhost', port, application, )