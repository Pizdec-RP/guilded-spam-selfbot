import subprocess

dir = "путь к папке в которй запущен бот"

for token in open(f"{dir}emailpass.txt","r").read().splitlines():
    subprocess.Popen(['python3',f'{dir}bot.py',token.split(':')[0],token.split(':')[1]])