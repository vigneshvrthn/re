import streamlit as st 
import pandas as pd
import pymongo

from streamlit_option_menu import option_menu
from datetime import datetime
with st.sidebar:    
    select_fun=option_menu("Menu",["cr","total"])


con=pymongo.MongoClient("mongodb://Vignesh:Vignesh3@ac-dsiib9v-shard-00-00.fvjkqe9.mongodb.net:27017,ac-dsiib9v-shard-00-01.fvjkqe9.mongodb.net:27017,ac-dsiib9v-shard-00-02.fvjkqe9.mongodb.net:27017/?ssl=true&replicaSet=atlas-l1j7no-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
dbs=con["aycsb"]
col=dbs["cr"]
if select_fun=="cr":
    date=st.date_input("date")
    name=st.text_input("enter the name")
    kl=st.text_input("entre the kl no")
    phone=st.number_input("enter the phone no",value=0, step=1)
    amt=st.number_input("enter the collected amt ",value=0, step=1)
    address=st.text_input("entre the address")
    date_as_datetime = datetime.combine(date, datetime.min.time())


    dic={"name":name,"address":address,"phone_no":phone,"amt":amt,"kl_no":kl,"date":date_as_datetime}

        
    
    if st.button("Print to PDF and save"):        
        col.insert_one(dic)
        st.write("sucessfully saved")
    
if select_fun=="total":
    date=st.date_input("date")
    date_as_datetime = datetime.combine(date, datetime.min.time())
    
    documents = [doc for doc in col.find({"date": date_as_datetime})]
    df=pd.DataFrame(documents)
    
    st.write(df)
