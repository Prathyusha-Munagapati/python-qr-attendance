  
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from playsound import playsound
import openpyxl
import datetime as dt
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
record = cv2.VideoCapture(0)
record.set(3,640)
record.set(4,480)

present_data=[]
