import requests, time
from PIL import Image
from pytesseract import *
import cv2
import numpy as np

def entry(carPlate):
	r = requests.post('http://127.0.0.1:8000/carentry/', data={"car_plate": carPlate})
	return r.status_code
def exit(carPlate):
	r = requests.post('http://127.0.0.1:8000/carexit/', data={"car_plate": carPlate})
	r.status_code
def query(carPlate):
	r = requests.post('http://127.0.0.1:8000/carquery/', data={"car_plate": carPlate})
	return r.content
