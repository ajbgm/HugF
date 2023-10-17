#python -m streamlit run MainUI.py  
import streamlit as st
import os
import Main
import time

def save_uploadedfile(uploadedfile):
     with open(os.path.join("Images",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
         return st.success("Image File saved successfuly")

st.title("Analyse images")
     
imgfile = st.file_uploader("Upload your image", type=['jpg'])
if imgfile is not None:
    save_uploadedfile(imgfile)
    st.write(imgfile.name)

if (st.button("Analyse the image")):
    imgpath = "./Images/" + imgfile.name
    
    with st.spinner('Please wait image analysis is in progress!!!'):
        result = Main.ProcessImage(imgpath)
        time.sleep(5)
        st.write("Image analysed....")
        st.write(result)
        if os.path.exists(imgpath):
           os.remove(imgpath)
     
        
