from flask_restful import Resource,Api
from flask import jsonify, request,Flask,Response
import requests
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
import json

#Handler general errors
class CustomApi(Api):
    def __init__(self, app:Flask ) -> None:
        super().__init__(app, catch_all_404s=True)
    def handle_error(self, err):
        if isinstance(err, HTTPException):
            return Response(json.dumps({
                    'message': getattr(
                        err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                    ),
                    'status':err.code
                }), mimetype='application/json'), err.code
        if not getattr(err, 'message', None):
            return Response(json.dumps({
                'message': 'Server has encountered some error',
                'status':500
                }), mimetype='application/json'), 500
        return Response(json.dumps(**err.kwargs), mimetype='application/json'), err.http_status_code