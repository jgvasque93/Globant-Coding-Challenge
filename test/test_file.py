from flask_testing import TestCase
from flask import current_app, url_for
from stopwatch import Stopwatch
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    #test if app exist
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    #test if app is in mode TESTING
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    #test if get to /artist with param name='coldplay' is success
    def test_success_get(self):
        response = self.client.get('/artist',query_string={"name": "coldplay"})
        self.assert200(response)

    #test if get to /artist with param name='coldplay' return header with content-type='application/json'
    def test_header_with_content_type_get(self):
        response = self.client.get('/artist',query_string={"name": "coldplay"})
        self.assertTrue(response.headers['Content-Type']=='application/json')

    #test if get to /artist with param name='' return error message and status 500
    def test_empty_name_get(self):
        response = self.client.get('/artist',query_string={"name": ""})
        assert(response.json['message']=='parameter name  null or blank' and response.json['status']==500)

    #test if get to /artist with param name null return error message and status 500
    def test_empty_null_get(self):
        response = self.client.get('/artist')
        assert(response.json['message']=='parameter name  null or blank' and response.json['status']==500)

    #test if get to /artist with param name not supported return error messahe and status 500
    def test_wrong_name_get(self):
        wrong_name='isnoartist'
        response = self.client.get('/artist',query_string={"name": wrong_name})
        assert(response.json['message']==f'error calling api https://www.theaudiodb.com/api/v1/json/2/search.php?s={wrong_name}' and response.json['status']==500)

    #test about performance from get /artist
    def test_performance_cache_name_get(self):
        stopwatch = Stopwatch(2)
        for x in range(0,100):
            self.client.get("/artist",query_string={"name": f"isnoartist{x}"})
        stopwatch.stop()
        time_random=stopwatch.duration
        stopwatch = Stopwatch(2)
        for x in range(0,100):
            self.client.get("/artist",query_string={"name": f"coldplay"})
        stopwatch.stop()
        time_constant=stopwatch.duration
        print(time_constant,time_random)
        self.assertTrue(time_constant-time_random <0)

    #test if get to != /artist return status 404
    def test_bad_endpoint(self):
        response = self.client.get('/badLink')
        self.assert404(response)