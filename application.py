#!/usr/bin/python
import sys
import json
import requests

def parse_json(json_object):

    parsed_json = json.loads(json_object)
    periods = parsed_json['properties']['periods']
    count = len(periods)
    count -= 1
    while count > -1:
        #print count
        print str(periods[count])
        count -= 1
    return count

def main():

    ####################
    # Define variables #
    ####################
    url = "https://api.weather.gov/gridpoints/FFC/51,87/forecast/hourly"
    #################
    # Make API call #
    #################
    r = requests.get(url)
    ###############
    # Get results #
    ###############
    json_object = r.content
    api_status = r.status_code
    api_url = r.url
    #################
    # Print results #
    #################
    print api_url
    print api_status
    result = parse_json(json_object)
    #print result

if __name__=="__main__":
    sys.exit(main())
