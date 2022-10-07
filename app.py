import streamlit as st
from rembg import remove

uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)

    image = uploaded_file.read()
    st.image(image)

    output_path = "scont_"+uploaded_file.name


    if st.button('Scontorna'):
        output = remove(image)
        
        st.image(output)
        #output.save(output_path)
        btn = st.download_button(
            label="Download image",
            data=output,
            file_name="scont_"+uploaded_file.name,
            mime="image/png")