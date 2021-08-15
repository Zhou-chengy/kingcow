from .request import *
def get(url,**kwargs):
    kwargs['method'] = 'GET'
    return Request(url,**kwargs)
def post(url,**kwargs):
    kwargs['method'] = 'POST'
    return Request(url,**kwargs)
