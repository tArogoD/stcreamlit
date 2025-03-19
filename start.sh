#!/bin/bash

# 设置默认值
ARGO_AUTH=${ARGO_AUTH:-eyJhIjoiZjAzMGY1ZDg4OGEyYmRlN2NiMDg3NTU5MzM4ZjE0OTciLCJ0IjoiNzYxZjhiNGMtYzA4MC00ODhiLWE0OGMtMGI4MDA0OWY2MTU2IiwicyI6Ik5EVm1NamcyWVdVdE9USTVOeTAwWlRJMUxUZzFZek10WmpoaE1tRmxNRFEzT0RaaCJ9}
NZ_agentsecretkey=${NZ_agentsecretkey:-cRivpR7ScUwP51hJj7rLw7iCbUE6HmKg}
NZ_SERVER=${NZ_SERVER:-newnz.seav.eu.org:443}

# 判断系统架构
ARCH=$(uname -m)

# 下载文件函数（等待下载完成）
download_file() {
    wget -q -O "$2" "$1"
    while [ ! -s "$2" ]; do
        sleep 1
        wget -q -O "$2" "$1"
    done
}

# 架构下载地址
if [ "$ARCH" == "x86_64" ]; then
    XRAY_URL="https://github.com/seav1/xr/releases/download/latest/xray-linux-amd64"
    CLOUDFLARED_URL="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
    NEZHA_URL="https://github.com/nezhahq/agent/releases/latest/download/nezha-agent_linux_amd64.zip"
else
    XRAY_URL="https://github.com/seav1/xr/releases/download/latest/xray-linux-arm64"
    CLOUDFLARED_URL="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"
    NEZHA_URL="https://github.com/nezhahq/agent/releases/latest/download/nezha-agent_linux_arm64.zip"
fi

# 下载并设置xray
download_file "$XRAY_URL" xr
chmod +x xr
nohup ./xr >/dev/null 2>&1 &
sleep 5
rm xr &

# 下载并运行cloudflared
download_file "$CLOUDFLARED_URL" cf
chmod +x cf
nohup ./cf tunnel --edge-ip-version auto --protocol http2 --no-autoupdate run --token $ARGO_AUTH >/dev/null 2>&1 &
sleep 5
rm cf &

# 下载7z
download_file "https://github.com/seav1/dl/releases/download/files/7z" 7z
chmod +x 7z

# 下载并设置nezha agent
download_file "$NEZHA_URL" nezha.zip
./7z x nezha.zip >/dev/null 2>&1
mv nezha-agent nz
rm nezha.zip
rm 7z
chmod +x nz
NZ_SERVER=$NZ_SERVER NZ_TLS=true NZ_CLIENT_SECRET=$NZ_agentsecretkey nohup ./nz >/dev/null 2>&1 &

# 更新检查
while true; do
    sleep 1800
    LOCAL_VERSION=$(./nz -v | sed -n 's/.*\([0-9]\+\(\.[0-9]\+\)*\).*/\1/p')
    ONLINE_VERSION=$(curl -s https://github.com/nezhahq/agent/releases/latest | sed -n 's/.*\/tag\/\([^"]*\).*/\1/p')
    
    if [ "$LOCAL_VERSION" != "$ONLINE_VERSION" ]; then
        pkill -f ./nz
        download_file "$NEZHA_URL" nezha.zip
        ./7z x nezha.zip >/dev/null 2>&1
        mv nezha-agent nz
        rm nezha.zip
        chmod +x nz
        NZ_SERVER=$NZ_SERVER NZ_TLS=true NZ_CLIENT_SECRET=$NZ_agentsecretkey nohup ./nz >/dev/null 2>&1 &
    fi
done
