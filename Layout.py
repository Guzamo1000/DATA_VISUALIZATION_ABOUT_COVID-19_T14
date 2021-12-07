import numpy as np #pip install numpy
from datetime import datetime #pip install DateTime
from numpy.core.fromnumeric import choose 
import pandas as pd #pip install pandas
# import matplotlib.pyplot as plt #pip install matplotlib
import streamlit as st #pip install streamlit
from streamlit.uploaded_file_manager import UploadedFile 
from PIL import Image  #python3 -m pip install --upgrade Pillow
import datetime 
@st.cache #using cache memory 
class Layout:
    """
    Create layout and return time properties
    """
    def __init__(self,img):
        self.img=img
    def Title():
        # hiden title to sidebar
        img=Image.open(r'download.jpg')
        st.sidebar.image(img)
        st.sidebar.header('Upload data about covid-19')
    # @st.cache
    def upload_data():
        """
        upload data from pc
        input: data
        output: variable containing data
        """
        upload=None
        upload=st.sidebar.file_uploader(label='Load data',type=['csv','xlsx'])
        if upload is not None:
             st.sidebar.success("Loading file Complete")
        return upload
        # data_country_daywise=pd.read_csv(r'E:\PTIT\HK1-N3\Python3\project\Data\Covid-19-Preprocessed-Dataset\preprocessed\country_daywise.csv')
        # data_countrywise=pd.read_csv(r'E:\PTIT\HK1-N3\Python3\project\Data\Covid-19-Preprocessed-Dataset\preprocessed\countrywise.csv')
        # data_cleaned=pd.read_csv(r'E:\PTIT\HK1-N3\Python3\project\Data\Covid-19-Preprocessed-Dataset\preprocessed\covid_19_data_cleaned.csv')
        # data_daywise=pd.read_csv(r'E:\PTIT\HK1-N3\Python3\project\Data\Covid-19-Preprocessed-Dataset\preprocessed\daywise.csv')
        # return data_country_daywise,data_countrywise,data_cleaned,data_daywise
    def time():
        """return realtime"""
        today=datetime.datetime.now()
        date=st.date_input('Time: ',datetime.datetime.now())
        return date
    def run_time():
        """return today and tomorrow"""
        time_first=datetime.datetime.now()
        time_last=time_first+ datetime.timedelta(days=1)
        start = st.date_input('Start date', time_first)
        end = st.date_input('End date', time_last)
        return start,end

