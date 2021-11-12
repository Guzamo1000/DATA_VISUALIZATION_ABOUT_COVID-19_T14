import numpy as np
from datetime import datetime
from numpy.core.fromnumeric import choose
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile
from PIL import Image
import datetime
@st.cache
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

