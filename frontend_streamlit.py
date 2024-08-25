import streamlit as st
import requests
import json

# Set the title of the Streamlit app
st.title('21BEC2013 JSON Processor')

# Input area for JSON data
json_input = st.text_area('Enter JSON:', '')

# Button to submit JSON data
if st.button('Submit'):
    try:
        # Parse JSON input
        parsed_data = json.loads(json_input)

        # Make a POST request to the Flask API
        response = requests.post('http://127.0.0.1:5000/bfhl', json=parsed_data)

        # Check if the request was successful
        if response.status_code == 200:
            response_data = response.json()

            # Show the dropdown options after successful response
            st.selectbox('Select Response Type:', ['Alphabets', 'Numbers', 'Highest Lowercase Alphabet'],
                         key='response_type')

            response_type = st.session_state.get('response_type')

            output = '<h3>Response:</h3>'
            if response_type == 'Alphabets' or response_type == 'All':
                output += f"<p>Alphabets: {json.dumps(response_data.get('alphabets', []))}</p>"
            if response_type == 'Numbers' or response_type == 'All':
                output += f"<p>Numbers: {json.dumps(response_data.get('numbers', []))}</p>"
            if response_type == 'Highest Lowercase Alphabet' or response_type == 'All':
                output += f"<p>Highest Lowercase Alphabet: {json.dumps(response_data.get('highest_lowercase_alphabet', []))}</p>"

            st.markdown(output, unsafe_allow_html=True)
        else:
            st.error(f"Error: {response.status_code}")
    except json.JSONDecodeError:
        st.error("Invalid JSON input. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

