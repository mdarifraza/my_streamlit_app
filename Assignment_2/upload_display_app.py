import streamlit as st
st.write("Upload and Display Image & video App")
st.title("Upload and Display Image & video App")
st.header("Upload your Image or video file")

image_file=st.file_uploader("Upload Image",type=["png","jpg","jpeg"])

if image_file is not None:
    st.image(image_file)
    st.success("Image uploaded successfully")
    

video_file=st.file_uploader("Upload video",type=["mp4","avi","mov"])
if video_file is not None:
    st.video(video_file)
    st.success("video uploaded successfully")
