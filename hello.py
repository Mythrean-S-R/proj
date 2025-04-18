import streamlit as myth
import pandas as pd 
from pygame import mixer
from streamlit_option_menu import option_menu

mixer.init()


mixer.music.load("proj\\assests_music\\RAINING IN ＮＡＧＯＹＡ (Lofi HipHop).mp3")
mixer.music.play()

import time
myth.markdown(
    "<hr><h1 style='text-align: center; color: teal;'>TEAM XD</h1><hr>", 
    unsafe_allow_html=True
)
myth.title("TEAM XD")
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
DANZA KUDURO hello
"""
if myth.button("another one"):
    mixer.music.load("proj\\assests_music\\Danza-Kuduro.mp3")
    mixer.music.play()

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

if myth.button("Stream data"):
    myth.write_stream(stream_data)