import streamlit as st
import pandas as pd
import random
import plotly.express as px
import time

def rerun():
    return
    
def classify():
    pass

   
def random_walk(steps, start):
    position = start
    walk = [position]
    
    for _ in range(steps):
        step = random.uniform(-0.1, 0.1)  
        position += step
        position = max(0, min(1, position)) 
        walk.append(position)
    
    return walk

st.title('Random Walk Datastream')

with st.sidebar:
    col1, col2 = st.columns([1,1])
    with col1:
        restart = st.button("Restart", on_click=rerun)
    with col2:
        classify = st.button("Classify", on_click=classify)
    st.divider()    
    knee = st.toggle("Add Kneepoint")
    trend = st.toggle("Trend")
    
plot_spot = st.empty()
start = random.uniform(0, 1)
df = pd.DataFrame({'value': start}, index=[0])

while True:
    next_start = df["value"].max()
    if next_start == 1:
        new_data = pd.DataFrame({'value': 1}, index=[0])
    else:
        next_step = random_walk(1, next_start)
        next_step = next_step[-1]
        new_data = pd.DataFrame({'value': next_step}, index=[0])
        
    df = pd.concat([df, new_data], ignore_index=True)
    fig = px.line(df, x=df.index, y=df.value)
    fig.add_hrect(y0=0.9, y1=0.95, line_width=0, fillcolor="red", opacity=0.1)
    fig.add_hrect(y0=0.95, y1=1, line_width=0, fillcolor="darkred", opacity=0.25)
    time.sleep(1)
        
    with plot_spot:
        st.plotly_chart(fig)