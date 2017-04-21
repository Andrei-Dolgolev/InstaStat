"""
Author: Alexander Osipenko
https://github.com/subpath
"""
# -*- coding: utf-8 -*-

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

