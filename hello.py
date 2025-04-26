
import streamlit as myth
import pandas as pd
import numpy as np
import altair as alt
import streamlit_option_menu
from streamlit_option_menu import option_menu
import time

with myth.sidebar:
    selected=option_menu(
        menu_title="Access Point",
        options=["Home","Projects","About Us","Contact Us"]

    )
if selected=="Home":
    myth.markdown(
    "<hr>",
        myth.image("assests_music/TEAM_XD.png", width=120),
    "<img src='assests_music/TEAM_XD.png' width='120'/>"
    "<h1 style='text-align: center; color: white;'>TEAM XD</h1>"
    "<h4 style='text-align: center;'>-We Build. We Code. We XD. 🚀</h4>""<hr>"
    "<h2>About Us</h2>"
    "<h4>We are TEAM XD — a group of passionate creators who build projects, solve problems," 
    "and grow together. From brainstorming to deployment, we do everything as one team. Collaboration is our superpower, and creativity is our fuel. 💡🚀</h4>",

unsafe_allow_html=True
)

    #myth.title("TEAM XD")
    #myth.write(":rainbow[hary is the owner of SRM]")
    # ✅ Streamlit-native audio player (works on cloud)
    
    
    myth.write(":rainbow[For some lofi beats click below]")
    with open("assests_music/RAINING IN ＮＡＧＯＹＡ (Lofi HipHop).mp3", "rb") as audio_file:
        myth.audio(audio_file.read(), format="audio/mp3")


    #if myth.button("Send balloons!"):
        #myth.balloons()

    
    myth.title("Datas")
    myth.write(
        pd.DataFrame({
            "PROJECTS": ["VIDOES", "WEBSITES", "EDITING"],
            "COUNT": [36, "=-=", 45],
        })
    )

    
    #df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    #c = (
     #   alt.Chart(df)
      #  .mark_bar()
       # .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    #)
    #myth.write(c)

    #if myth.button("pani poliyum neram idhu"):
        #myth.snow()

    #_LOREM_IPSUM = "DANZA KUDURO hello"
    
    
    myth.markdown("<hr>",unsafe_allow_html=True)
    myth.write(":rainbow[For Another Song]")
    if myth.button("another one"):
        with open("assests_music/Danza-Kuduro.mp3", "rb") as audio_file:
            myth.audio(audio_file.read(), format="audio/mp3")

    
    
    #def stream_data():
        #for word in _LOREM_IPSUM.split(" "):
          #  yield word + " "
           # time.sleep(0.02)
    #if myth.button("Stream data"):
     #   myth.write_stream(stream_data)


if selected=="Projects":
    myth.title("Creations of TEAM XD")
    myth.video("https://youtu.be/4in2X_BWUX0?si=P7oU5PQHMU7oGS6W")
    myth.video("https://youtu.be/3DMuHOcKO2E?si=1S2sfiC3fAYtZqtJ")
    myth.video("https://youtu.be/eDKceY7r-LI?si=A7vgOGLelSb3iXGl")
    myth.video("https://youtu.be/MiclYFbhOIk?si=eMKzUVFAxdHUoSDC")
    myth.video("https://youtu.be/lADJ8eveeCA?si=B4DDIo5DsS1PFnMX")
    myth.video("https://youtu.be/IWPN21kB_ZA?si=jql7hd8EkZBP-3Yr")


if selected=="About Us":
    myth.title("About Us")
    myth.header('''Welcome to TEAM XD - a squad of curious minds, creative thinkers, and passionate builders. We're not just a team; we're a family that codes, creates, and grows together. 💡⚙️🎨

At TEAM XD, we:

Build cool projects with heart and hustle ❤️‍🔥

Learn together, fail together, win together 🛠️

Turn ideas into impactful tech 🚀

Bring good vibes to every line of code 🎧✨

We don’t just collaborate — we vibe, we grind, and we level up as one. Whether it’s designing, developing, or dreaming big — we do it together. Always.

💬 “One team. One dream. All in. That’s XD.''')
if selected=="Contact Us":
    myth.title("Contact Us")
    myth.header("Email: rcg4042@gmail.com")
    
