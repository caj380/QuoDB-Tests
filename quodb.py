import urllib2
import json
import sys

def time(time):
	millis=str(time)
	millis = int(millis)
	seconds=(millis/1000)%60
	seconds = int(seconds)
	minutes=(millis/(1000*60))%60
	minutes = int(minutes)
	hours=(millis/(1000*60*60))%24

	return ("%02d:%02d:%02d" % (hours, minutes, seconds))

commandStr = sys.argv[1] #"amazon offers one"

args = commandStr.split()

if len(args) > 0:

	searchTerm = "%20".join(args) # %20 -> espace

	searchUrl = "http://api.quodb.com/search/" + searchTerm + "?titles_per_page=1000&phrases_per_title=1000&page=1"
	#print("searchUrl : " + searchUrl)

	request = urllib2.Request(searchUrl)
	response = urllib2.urlopen(request)

	str_response = response.read().decode('utf-8')
	objJSON = json.loads(str_response)

	#print(str_response)

	if objJSON["numFound"] > 0:
		for JSON in objJSON["docs"]:
			if JSON["serie"]:
				series = JSON["serie"]
				print series
			movieTitle = JSON["title"]
			movieQuote = JSON["phrase"]
			quoteTime = JSON["time"]
			quotetime = time(quoteTime)
			print movieTitle
        		print movieQuote
    	    		print quotetime
			print "----------"	
	#print movieTitle
	#print movieQuote
	#print quotetime
