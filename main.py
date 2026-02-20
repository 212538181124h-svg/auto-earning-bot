import threading
import time
import requests
from flask import Flask
import os

app = Flask('')

# 1. Renderのスリープ防止（14分おきに自分を叩き起こす）
def keep_alive():
    while True:
        try:
            # Renderで割り当てられるURLを自動取得するか、localhostを叩く
            requests.get("http://localhost:10000")
            print("Self-ping sent: System is awake.")
        except:
            pass
        time.sleep(840) # 14分

# 2. AIバウンティ監視（日銭稼ぎ）
def bounty_agent():
    while True:
        # ここにタスク監視ロジックが走ります
        print("Bounty Agent: Scanning for new tasks...")
        time.sleep(3600)

# 3. エアドロップ巡回（将来の資産）
def airdrop_hunter():
    while True:
        # ここにテストネット巡回ロジックが走ります
        print("Airdrop Hunter: Performing automated transactions...")
        time.sleep(7200)

@app.route('/')
def home():
    return "AI Earning System: Running 24/7"

def run():
    # Renderは10000番ポートを使用します
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # 各機能を別スレッドで同時並行稼働
    threading.Thread(target=run).start()
    threading.Thread(target=keep_alive).start()
    threading.Thread(target=bounty_agent).start()
    threading.Thread(target=airdrop_hunter).start()
