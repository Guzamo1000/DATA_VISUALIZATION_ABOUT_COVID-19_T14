import numpy as np #pip install numpy
import pandas as pd #pip install pandas
import streamlit as st #pip install streamlit
import matplotlib.pyplot as plt #pip install matplotlib
#pip install plotly
import plotly.express as px 
import plotly.graph_objects as go


@st.cache
class Line:
    def __init__(self,df):
        self.df=df
    def Data_preprocessing_word(df):
        df=df.drop(columns=['Province/State','Lat','Long'])
        df=df.groupby(by='Date').aggregate(np.sum)
        df.index.name='Date'
        df=df.reset_index()
        return df
    def Data_preprocessing_country(df):
        df=df.drop(columns=['Province/State','Lat','Long'])
        df=df.groupby(by=['Country','Date']).aggregate(np.sum)
        df.index.name='Country'
        df=df.reset_index()
        return df
    def chart_line_all(self,day_first,day_lats):
        time=[]
        Confirmed=[]
        Deaths=[]
        Recovered=[]
        flag=False

        for i in range(0,len(self.df)):
            if (self.df['Date'][i]>=day_first and self.df['Date'][i]<=day_lats):
                time.append(self.df['Date'][i])
                Confirmed.append(self.df['Confirmed'][i])
                Deaths.append(self.df['Deaths'][i])
                Recovered.append(self.df['Recovered'][i])
                flag=True
            else: continue
        if flag==False: 
            st.error('Country not found or time not in data :(')
            return None
        else:
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=time,y=Confirmed,mode='lines+markers',name='Confirmed'))
            fig.add_trace(go.Scatter(x=time,y=Deaths,mode='lines+markers',name='Deaths'))
            fig.add_trace(go.Scatter(x=time,y=Recovered,mode='lines+markers',name='Recovered'))
            return fig
    def chart_line_country(self,country,day_first,day_last):
        """
        Create chart line
        """
        time=[]
        Confirmed=[]
        Deaths=[]
        Recovered=[]
        flag=False
        for i in range(0,len(self.df)):
            if self.df['Country'][i].lower()==country.lower() and (self.df['Date'][i]>=day_first and self.df['Date'][i]<=day_last):
                time.append(self.df['Date'][i])
                Confirmed.append(self.df['Confirmed'][i])
                Deaths.append(self.df['Deaths'][i])
                Recovered.append(self.df['Recovered'][i])
                flag=True
            else: continue
        if flag==False: 
            st.error('Country not found or time not in data :(')
            return None
        else:
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=time,y=Confirmed,mode='lines+markers',name='Confirmed'))
            fig.add_trace(go.Scatter(x=time,y=Deaths,mode='lines+markers',name='Deaths'))
            fig.add_trace(go.Scatter(x=time,y=Recovered,mode='lines+markers',name='Recovered'))
            return fig

