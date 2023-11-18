import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["harsh","Gupta"],
    "age":[21,32],
    "city":["noida","delhi"]
}

data = pd.read_csv("data//data.csv")

st.dataframe (data)