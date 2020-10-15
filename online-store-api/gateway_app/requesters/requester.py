import requests
import json
import re


class Requester:
	HOST = 'http://127.0.0.1'
	BASE_HTTP_ERROR = (json.dumps({'error': 'BaseHTTPError'}), 500)

	def get_request(self, url, headers: dict={}):
		try:
			response = requests.get(url, headers=headers)
		except (requests.exceptions.BaseHTTPError, requests.exceptions.ConnectionError):
			return None
		return response

	def post_request(self, url, data: dict = {}, headers: dict={}):
		try:
			response = requests.post(url, headers=headers, data=data)
		except (requests.exceptions.BaseHTTPError, requests.exceptions.ConnectionError):
			return None
		return response

	def get_data_from_response(self, response):
		try:
			return response.json()
		except (ValueError, json.JSONDecodeError, AttributeError):
			return response.text

	def get_token_from_request(self, request):
		token_str = request.META.get('HTTP_AUTHORIZATION')
		try:
			token = token_str[6:].strip()
		except TypeError:
			return None
		return token
