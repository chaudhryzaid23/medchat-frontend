import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# hashed_passwords = stauth.Hasher.hash_passwords(config['credentials'])
# print(hashed_passwords)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

authenticator.login('main')

# add session id and chat ui here along with call

# logout will be top for this case

name = st.session_state["name"]
authentication_status = st.session_state['authentication_status']

if authentication_status:
    if name == 'John Smith':
        st.write(f'Welcome *{name}*')
        st.title('Application 1')
    elif name == 'rbriggs':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
    authenticator.logout()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')