import http.client
import json

conn = http.client.HTTPConnection('localhost',5050)

def getLeaderBoard(token):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    conn.request('GET', '/ranking',None, headers)
    response = conn.getresponse()
    return response
    
def getPersonalStats(token):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    conn.request('GET', '/stats',None, headers)
    response = conn.getresponse()
    return response