
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth

# hashed_passwords = stauth.Hasher(['abcd', '1234']).generate()
# print(hashed_passwords)

# with open('./config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# authenticator.login('Login', 'main')

# print("authentication_status:", st.session_state["authentication_status"])

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main', key='unique_key')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password(st.session_state["username"], 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)