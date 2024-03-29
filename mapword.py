# import pandas as pd                                 #pip install pandas
# import numpy as np
import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st
# import matplotlib.pyplot as plt
import folium                                       #pip install folium
from streamlit_folium import folium_static          #pip install streamlit_folium
# @st.cache
class Map:
        def __init__(self,df):
                # create a map
                # input 
                #   df:  data input
                #   date: date sreach
                self.m = folium.Map(location=[0, 0], tiles='cartodbpositron', min_zoom = 1, max_zoom=10, zoom_start=2)
                self.df = df
                self.date1=None


        # def xl(self):
        #         for i in range(len(self.df)):
        #                 if df['Date'][i]==
        def datamap(self,date1):
                self.date1 = date1
                flag=0
                for i in range(0, len(self.df)):
                        if self.df['Date'][i]==self.date1:
                                
                                folium.Circle(location=[self.df.iloc[i]['Lat'], self.df.iloc[i]['Long']],color ='red', fill='crimson',
                                        tooltip='<li><bold> Country: ' + str(self.df.iloc[i]['Country'])+
                                                        '<li><bold> Province: ' + str(self.df.iloc[i]['Province/State'])+
                                                        '<li><bold> Confirmed: ' + str(self.df.iloc[i]['Confirmed'])+
                                                        '<li><bold> Deaths: ' + str(self.df.iloc[i]['Deaths']),
                                                radius = int(self.df.iloc[i]['Confirmed'])**0.7).add_to(self.m) 
                                flag+=1                
                                                
                        else:
                                continue
                        
                if flag!=0:
                        return self.m
                else: return 0
        def datatop(self):
                confirmed_dl=self.df.drop(columns=['Lat','Long','Province/State','Recovered','Deaths','Active'])
                max_date = confirmed_dl['Date'].max()
                total_confirmed_df = confirmed_dl[confirmed_dl['Date'] == max_date]
                fig = px.choropleth(total_confirmed_df,
                    locations='Country', locationmode='country names',
                    # color_continuous_scale='dense',
                    color= total_confirmed_df['Confirmed'])
                return fig  