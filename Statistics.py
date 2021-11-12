import numpy as np
import pandas as pd

class Statistical_data_visualization:
    def __init__(self,df):
        self.df=df
    def Data_preprocessing(self):
        """
        Data processing before extraction
        input: 
            value: name column
        output: 
            value column is the column to be processed (ct: Country, days: Date)
        """
        ct=self.df.drop(columns=['Province/State','Lat','Long']).copy()
        days=self.df.drop(columns=['Province/State','Lat','Long']).copy()
        ct=ct.groupby(by=['Country']).aggregate(np.sum)
        days=days.groupby(by=['Date']).aggregate(np.sum)

        ct.index.name='Country'
        days.index.name='Date'
        ct=ct.reset_index()
        days=days.reset_index()
        return ct,days
    def total_country(self,ct):
        num=0
        for i in range(len(ct)):
            if ct['Confirmed'][i]==0: num+=1
        return num
    def By_country(self,data,inf):
        """
        Calculate the largest, smallest, and number of countries
        input:
            data: Data has been processed
            inf: Comparative information
        output:
            return the country with the largest number of inf and the number of inf
            return the country with the smallest number of inf and the number of inf
        """
        inf_max=0
        inf_min=max(data[inf])
        id_max=None
        id_min=None
        Country_none=None
        for i in range(len(data)):
            if data[inf][i]>inf_max:
                inf_max=data[inf][i]
                id_max=i
            if data[inf][i]<inf_min:
                inf_min=data[inf][i]
                id_min=i
        return data['Country'][id_max] , inf_max , data['Country'][id_min] , inf_min
    def Date_handling(self,data,inf):
        """
        Calculate values for date
        input: 
            data: Data has been processed
            inf: Information to be processed
        output:
            return average
            return maximum by day 
            return Lowest by day
        """
        ave=[]
        day_max=0
        id_max=None
        day_min=max(data[inf])
        id_min=None
        for i in range(1,len(data)):
            if i >=1 and (data[inf][i]-data[inf][i-1]>0):
                ave.append(data[inf][i]-data[inf][i-1])
            if data[inf][i]>day_max:
                day_max=data[inf][i]
                id_max=i
            if data[inf][i]<day_min:
                day_min=data[inf][i]
                id_min=i
        return (sum(ave)/len(ave)), day_max , day_min, data['Date'][id_max],data['Date'][id_min]
    def by_country(self,country,inf):
        date_max=0
        date_min=100000000000000
        id_date_max=None
        id_date_min=None
        ave=[]
        for i in range(len(self.df)):
            if self.df['Country'][i]==country and self.df[inf][i] > date_max:
               date_max=self.df[inf][i]
               id_date_max=i
            if self.df['Country'][i]==country and self.df[inf][i] < date_min:
                date_min=self.df[inf][i]
                id_date_min=i
            if self.df['Country'][i]==country and i>=1:
                ave.append(self.df[inf][i]-self.df[inf][i-1])
        return date_max,date_min,self.df['Date'][id_date_max],self.df['Date'][id_date_min],sum(ave)/len(ave)
    def find_coutry(self, country):
        for i in range(len(self.df['Country'])):
            if self.df['Country'][i].lower()==country.lower(): return True
        return False