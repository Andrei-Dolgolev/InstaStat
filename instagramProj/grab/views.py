# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the grab index.")


def graph(request):
    return render(request, 'graph/graph.html')

def PyData(request):
    print "start_load"
    username='ladygaga'
    url0 = ''.join(['https://www.instagram.com/', username, '/media/'])
    r = requests.get(url0)
    data = json.loads(r.text)['items']
    for i in range(1):# позже попробывать по 5 в grequest
        print 'i'
        last_id = data[-1]['id']
        url = ''.join(['https://www.instagram.com/', username, '/media?max_id=', last_id, '?more_available=True'])
        r = requests.get(url)
        d = json.loads(r.text)
        for item in d['items']:
            data.append(item)
        if last_id == data[-1]['id']:
            break
    print data
    print "end"

    Y=[0,3,1,2,4,5,5,6,6]
    X=[0,1,2,3,4,5,6,7,8]

    data={'Y':Y,'X':X}
    return JsonResponse(data)

"""
def play_count_by_month(request):
    data = Play.objects.all() \
        .extra(select={'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')}) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)
"""
"""
import requests
import json
from geopy.geocoders import Nominatim
from datetime import datetime


def get_all_posts(username):
	url0 = ''.join(['https://www.instagram.com/',username,'/media/'])
	r = requests.get(url0)
	data = json.loads(r.text)['items']
	for i in range(100):
		last_id = data[-1]['id']
		url = ''.join(['https://www.instagram.com/', username , '/media?max_id=' , last_id, '?more_available=True'])
		r = requests.get(url)
		d = json.loads(r.text)
		for item in d['items']:
			data.append(item)
		if last_id == data[-1]['id']:
			break
	return data

def update_data_with_coordinates(data):
	geolocator = Nominatim()
	for i in range(len(data)):
		try:
			loc = data[i]['location']['name'].decode('utf-8')
			location = geolocator.geocode(loc)
			lat = location.latitude
			lon = location.longitude
			data[i]['coordinates'] = [lon, lat]
		except:
			pass
	return data


def reshape_for_plotting(data):
	locations = []
	lat = []
	lon = []
	created_time = []
	likes = []
	comments = []
	thumbnail = []
	low_resolution = []
	user = {}
	for i in data:
		try:
			locations.append(i['location']['name'].decode('utf-8'))
			lat.append(i['coordinates'][1])
			lon.append(i['coordinates'][0])
		except:
			pass
	for i in data:
		created_time.append(datetime.fromtimestamp(float(i['created_time'])))
		likes.append(int(i['likes']['count']))
		comments.append(i['comments']['count'])
		thumbnail.append(i['images']['thumbnail']['url'])
		low_resolution.append(i['images']['low_resolution']['url'])
	user['fullname'] = data[0]['user']['full_name']
	user['profile_picture'] = data[0]['user']['profile_picture']


	return {"locations": locations, 
			'lat': lat,
			'lon': lon,
			'created_time':created_time,
			'likes': likes,
			'comments': comments,
			'thumbnail': thumbnail,
			'low_resolution': low_resolution,
			'user': user,
						}
"""

