import os
import paramiko
import requests
import json
from datetime import datetime, timezone, timedelta

def ssh_multiple_connections(hosts_info, command):
    users = []
    for host_info in hosts_info:
        hostname = host_info['hostname']
        username = host_info['username']
        password = host_info['password']
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, port=22, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command(command)
            user = stdout.read().decode().strip()
            users.append(user)
            ssh.close()
        except Exception as e:
            print(f"连接 {hostname} 时出错: {str(e)}")
    return users

hosts_info = []
ssh_info_str = os.getenv('SSH_INFO', '[]')
hosts_info = json.loads(ssh_info_str)

command = 'whoami'
user_list = ssh_multiple_connections(hosts_info, command)

beijing_timezone = timezone(timedelta(hours=8))

time = datetime.now(beijing_timezone).strftime('%Y-%m-%d %H:%M:%S')

loginip = requests.get('https://api.ipify.org?format=json').json()['ip']

pushplus_token = os.getenv('PUSHPLUS_TOKEN')

title = 'serv00 服务器登录提醒'
content = f"用户：{', '.join(user_list)}, 登录了 SSH 服务器<br>登录时间：{time}<br>登录IP：{loginip}"
url = 'http://www.pushplus.plus/send'
data = {
    "token": pushplus_token,
    "title": title,
    "content": content
}
body = json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=body, headers=headers)
if response.status_code == 200:
    print("推送成功")
else:
    print(f"推送失败，状态码: {response.status_code}")
