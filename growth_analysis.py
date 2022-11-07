import pandas as pd
import time
import datetime
import streamlit as st 

df1 = pd.read_csv("kabu探ファイル\prime.csv",encoding="cp932")
df2 = pd.read_csv("kabu探ファイル\standard.csv",encoding="cp932")
df3 = pd.read_csv("kabu探ファイル\growth.csv",encoding="cp932")

st.title("Growth_分析")
st.caption("業績推移ファンダメンタル分析")

code00 = st.text_input("証券コード入力")   
    
submit_button = st.button("Enter")
if submit_button:
        
    try:
        st.table(df1[["列1",f"{code00}"]])
     
    except:
        pass
    
    try:
        st.table(df2[["Unnamed: 0",f"{code00}"]])
     
    except:
        pass
    
    try:
        st.table(df3[["Unnamed: 0",f"{code00}"]])
     
    except:
        pass
       
    
#st.caption("prime市場")
#st.write(df1)
#"---"
#st.caption("standard市場")
#st.write(df2)
"---"
#st.caption("growth市場")
#st.write(df3)
