import streamlit as st
import requests

st.title('JSON Processor')

json_input = st.text_area('Enter JSON:', '{}')

if st.button('Submit'):
    try:
        # Parse JSON
        data = eval(json_input)
        response = requests.post('http://127.0.0.1:5000/bfhl', json=data)
        if response.status_code == 200:
            result = response.json()
            st.write(result)
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Invalid JSON input. Please try again. Error: {str(e)}")
