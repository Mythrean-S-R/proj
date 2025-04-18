import streamlit as myth
import pandas as pd 
import time
myth.write("hary is super robot")
myth.write(":rainbow[hary is the owner of SRM]")
if myth.button("Send balloons!"):
    myth.balloons()
myth.video(data="https://youtu.be/4in2X_BWUX0?si=P7oU5PQHMU7oGS6W")
myth.write(
    pd.DataFrame(
        {
            "first_Coloumn":[1,0,2,3],
            " :camera: second":[45,56,67,78],
        }
    )
)
import numpy as np
import altair as alt

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_bar()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

myth.write(c)
if myth.button("pani poliyum neram idhu"):
    myth.snow()
_LOREM_IPSUM = """
DANZA KUDURO
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    if myth.button("play music"):
        myth.audio(data=r"C:\Users\MYTHREAN\Downloads\Danza-Kuduro.mp3")
    

if myth.button("Stream data"):
    myth.write_stream(stream_data)