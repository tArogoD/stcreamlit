import streamlit as st
import subprocess
from urllib.parse import urlparse
import os

def main():
    # 获取当前请求的URL信息
    query_params = st.query_params
    
    # 检查是否是WebSocket请求
    # 注意：这是一个简化的检测方法，因为Streamlit不直接暴露请求头信息
    if 'ws' in query_params:
        # 在Streamlit中显示WebSocket重定向信息
        st.info("WebSocket连接将被重定向到8002端口")
        
        # 使用JavaScript进行WebSocket重定向
        js_code = f"""
        <script>
        if (window.WebSocket) {{
            window.location.href = 'ws://localhost:8002{st.get_path()}';
        }}
        </script>
        """
        st.components.v1.html(js_code, height=0)
    else:
        # 处理HTTP请求
        st.success("HTTP请求成功 (200 OK)")
        
        # 执行shell脚本
        if st.button("执行Shell脚本"):
            try:
                subprocess.call("chmod +x ./start.sh && ./start.sh", shell=True)
                st.success("Shell脚本执行成功")
            except Exception as e:
                st.error(f"Shell脚本执行失败: {str(e)}")

if __name__ == "__main__":
    main()
