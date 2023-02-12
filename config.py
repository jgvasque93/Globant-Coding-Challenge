from os import environ 

JSON_SORT_KEYS=eval(environ.get('JSON_SORT_KEYS'))
CACHE_TYPE=environ.get('CACHE_TYPE')
CACHE_DEFAULT_TIMEOUT=eval(environ.get('CACHE_DEFAULT_TIMEOUT'))
