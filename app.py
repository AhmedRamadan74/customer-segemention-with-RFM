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
df=pd.read_csv("Cleaned_Data_Merchant_Name.csv")
df_rfm=pd.read_csv("df_rfm.csv")# data that has RFM  and cluster


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
num_rec=st.number_input("Please enter number of recomendation ",min_value=1)

#backend function to recommend best three merchant
#num_mer is number of recommandation to merchant
def recommend_mer(user_id,num_mer):
    if df_rfm[df_rfm["User_Id"]==user_id]["dbscan"].values[0]=='only_F&B':
        F_B=df[df["Category In English"]=="F&B"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        #print
        st.write("You can spend your points in Food and beverage with : ")
        for i,mer in enumerate(F_B,1):
            st.write(f"{i} - {mer}")
            
    elif df_rfm[df_rfm["User_Id"]==user_id]["dbscan"].values[0]=='only_Fashion':
        Fashion=df[df["Category In English"]=="Fashion"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        #print 
        st.write("You can spend your points in Fashion with : ")
        for i,mer in enumerate(Fashion,1):
            st.write(f"{i} - {mer}")
                
    elif df_rfm[df_rfm["User_Id"]==user_id]["dbscan"].values[0]=='only_Grocery':
        Grocery=df[df["Category In English"]=="Grocery"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        #print 
        st.write("You can spend your points in Grocery with : ")
        for i,mer in enumerate(Grocery,1): 
            st.write(f"{i} - {mer}")
            
    elif df_rfm[df_rfm["User_Id"]==user_id]["dbscan"].values[0]=='only_Health&Beauty':
        Health_Beauty=df[df["Category In English"]=='Health & Beauty']["Mer_Name"].value_counts().head(num_mer).index.tolist()  
        #print 
        st.write("You can spend your points in Health&Beauty with : ")
        for i,mer in enumerate(Health_Beauty,1):
            st.write(f"{i} - {mer}")
            
    else:# dbscan=='all_Categories'
        F_B=df[df["Category In English"]=="F&B"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        Fashion=df[df["Category In English"]=="Fashion"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        Grocery=df[df["Category In English"]=="Grocery"]["Mer_Name"].value_counts().head(num_mer).index.tolist()
        #print 
        st.write("You can spend your points in Grocery , Food and beverage and Fashion with : ")
        st.write("With Grocery : ")
        for i,mer in enumerate(Grocery,1):
            st.write(f"{i} - {mer}")
            
        st.write("*"*5)    
        st.write("with Food and beverage : ")
        for i,mer in enumerate(F_B,1):
            st.write(f"{i} - {mer}")
            
        st.write("*"*5)    
        st.write("with Fashion : ")
        for i,mer in enumerate(Fashion,1):
            st.write(f"{i} - {mer}") 

recommend_mer(user_id,num_rec)