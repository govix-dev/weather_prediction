import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genny
from PIL import Image

load_dotenv()
key=os.getenv("key")

genny.configure(api_key=key)
model = genny.GenerativeModel("gemini-1.5-flash")

st.set_page_config(layout="wide", page_title="GeoSync")

st.sidebar.title("GeoSync")
st.sidebar.write("## Upload the image :gear:")
response_placeholder = st.empty()


def submit():
    st.markdown("Result")
    if my_upload:
        image = Image.open(my_upload)
        prompt = f"This is a image from a geostationary weather satellite called'{source}'.Predict the weather condition in the Indian subcontinent and explain details about the cloud details and is there any sign of cyclone formation or any other abnormality."
        response = model.generate_content([image, prompt])
        st.write(response.text)
        st.write(source)
    else:
        st.warning("Please upload an image before submitting.")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
source=st.sidebar.selectbox("Select a source",["Fengyun-2H","Elektro-L3"],index=0)
st.sidebar.button("Submit", on_click=submit)
