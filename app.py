import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import sklearn
import plotly.express as px
import xgboost
import joblib
import itertools

#read data
df_orginal=pd.read_csv("Cleaned_Data_Merchant_Name.csv")
df_rfm=pd.read_csv("df_rfm.csv")# data that has RFM 
data_cat=pd.read_csv("data_cat.csv") # recommend mer name for each category depends on clustering

#layout
st.set_page_config(page_title="Customer Segmention",layout="wide")


row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Customer Segmention')
    st.markdown(''' <h6>
                    This application was created to divide customer data into categories based on points and the total orders made by the customer and recommend the best merchants for each user as targetted offers.  </center> </h6> ''', unsafe_allow_html=True)
with row0_2:
    st.text("")
    st.subheader('Linkedin : App by [Ahmed Ramadan](https://www.linkedin.com/in/ahmed-ramadan-18b873230/) ')
    st.subheader('Github : App by [Ahmed Ramadan](https://github.com/AhmedRamadan74/customer-segemention-with-RFM)')

user_id=st.selectbox("Please enter you ID :",df_rfm["User_Id"].unique())

total_point=df_orginal[df_orginal["User_Id"]==user_id]["Points"].sum()

st.write(f"You have {total_point} points ")
st.write("*"*5)
#backend function to recommend best three merchant
def recommend_mer(user_id):

    #category for each clustering 
    #list have mer_name for each Category 
    Grocery_0=data_cat[(data_cat['kmean_id']==0) & (data_cat['Category In English']=="Grocery")]["Mer_Name"].tolist()
    F_B_0=data_cat[(data_cat['kmean_id']==0) & (data_cat['Category In English']=="F&B")]["Mer_Name"].tolist()
    Fashion_0=data_cat[(data_cat['kmean_id']==0) & (data_cat['Category In English']=="Fashion")]["Mer_Name"].tolist()

    Grocery_1=data_cat[(data_cat['kmean_id']==1) & (data_cat['Category In English']=="Grocery")]["Mer_Name"].tolist()

    Grocery_2=data_cat[(data_cat['kmean_id']==2) & (data_cat['Category In English']=="Grocery")]["Mer_Name"].tolist()
    F_B_2=data_cat[(data_cat['kmean_id']==2) & (data_cat['Category In English']=="F&B")]["Mer_Name"].tolist()
    Fashion_2=data_cat[(data_cat['kmean_id']==2) & (data_cat['Category In English']=="Fashion")]["Mer_Name"].tolist()

    Grocery_3=data_cat[(data_cat['kmean_id']==3) & (data_cat['Category In English']=="Grocery")]["Mer_Name"].tolist()
    F_B_3=data_cat[(data_cat['kmean_id']==3) & (data_cat['Category In English']=="F&B")]["Mer_Name"].tolist()
    Fashion_3=data_cat[(data_cat['kmean_id']==3) & (data_cat['Category In English']=="Fashion")]["Mer_Name"].tolist()
    
    #Get all cluserting for user
    kmeans=df_rfm[df_rfm["User_Id"]==user_id]["kmean_id"].unique()
    Grocery=[]
    F_B=[]
    Fashion=[]
    for kmean in kmeans:
        if kmean==0:
            Grocery.append(Grocery_0)
            F_B.append(F_B_0)
            Fashion.append(Fashion_0)
        if kmean==1:
            Grocery.append(Grocery_1)
        if kmean==2:
            Grocery.append(Grocery_2)
            F_B.append(F_B_2)
            Fashion.append(Fashion_2)
        if kmean==3:
            Grocery.append(Grocery_3)
            F_B.append(F_B_3)
            Fashion.append(Fashion_3)
    #to convert from 3-d to 1d list , convert from set to list because drop dulipcted
    Grocery=set(list(itertools.chain(*Grocery))) 
    F_B=set(list(itertools.chain(*F_B)))
    Fashion=set(list(itertools.chain(*Fashion)))
    
    st.write("We recommended for you spend points in ")
    
    st.write("In Grocery You have : ")
    for Grocery in Grocery:
        st.write(Grocery)

    st.write("*"*5)
    st.write("In food and beverage You have : ")
    for food in F_B:
        st.write(food)
    st.write("*"*5)
    st.write("In Fashion You have : ")
    for Fashion in Fashion:
        st.write(Fashion)

recommend_mer(user_id)