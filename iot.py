import urllib2
import calendar
import time
import json
url=”https://rfidbsp.firebaseio.com/rfid”
def locat(loc, rfid):
	postdata = {
		‘time’: time.strftime(“%A %B %d, %Y %H:%M:%S”)
			‘location’: loc,
		‘id’: rfid
	}
	req= urllib2.Request(url)
	req.add_header(‘Content-Type’,’application/json’)
	data = json.dumps(postdata)
response=urllib2.urlopen(req,data)
