import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


@st.cache
class Line:
    def __init__(self,df,country,time_start,time_end):
        self.df=df.copy()
        self.country=country
        self.time_start=time_start
        self.time_end=time_end
    def chart_line(self):
        """
        Create chart line
        """
        time=[]
        Confirmed=[]
        Deaths=[]
        Recovered=[]
        flag=False
        for i in range(0,len(self.df)):
            if self.df['Country'][i].lower()==self.country.lower():
                if self.df['Date'][i]>self.time_start and self.df['Date'][i]<self.time_end:
                    time.append(self.df['Date'][i])
                    Confirmed.append(self.df['Confirmed'][i])
                    Deaths.append(self.df['Deaths'][i])
                    Recovered.append(self.df['Recovered'][i])
                    flag=True
        if flag==False: 
            st.error('Country not found or time not in data :(')
            return None
        else:
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=time,y=Confirmed,mode='lines+markers',name='Confirmed'))
            fig.add_trace(go.Scatter(x=time,y=Deaths,mode='lines+markers',name='Deaths'))
            fig.add_trace(go.Scatter(x=time,y=Recovered,mode='lines+markers',name='Recovered'))
            return fig
    

