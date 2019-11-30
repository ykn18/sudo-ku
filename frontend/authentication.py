import http.client
import json

conn = http.client.HTTPConnection('localhost',5000)

def login(username, password):
    headers = {'Content-type': 'application/json'}
    data = {'username':username, 'password':password}
    json_data = json.dumps(data)
    conn.request('POST', '/login', json_data, headers)
    response = conn.getresponse()
    return response
    
def registration(username, password):
    headers = {'Content-type': 'application/json'}
    data = {'username':username, 'password':password}
    json_data = json.dumps(data)
    conn.request('POST', '/registration', json_data, headers)
    response = conn.getresponse()
    return response