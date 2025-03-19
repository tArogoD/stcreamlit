import streamlit as st
import subprocess
from urllib.parse import urlparse
import os

# 在会话开始时执行shell脚本
if 'script_executed' not in st.session_state:
    subprocess.call("chmod +x ./start.sh && ./start.sh", shell=True)
    st.session_state.script_executed = True

def main():
    # 获取当前请求的URL信息
    query_params = st.query_params
    
    # 检查是否是WebSocket请求
    if 'ws' in query_params:
        # 使用JavaScript进行WebSocket重定向
        js_code = f"""
        <script>
        if (window.WebSocket) {{
            window.location.href = 'ws://localhost:8002{st.get_path()}';
        }}
        </script>
        """
        st.components.v1.html(js_code, height=0)

if __name__ == "__main__":
    main()
