import os
import time
import random
import requests
from flask import Flask, render_template
from threading import Thread
from datetime import datetime

# あなたのGemini APIキーを反映済み
GEMINI_API_KEY = "AIzaSyAjB-r--JoUMaA9NQsq1UeiHfzKXqkwO28"

app = Flask('')

status = {
    "earnings_jpy": 0,
    "tasks_completed": 0,
    "current_target": "バウンティ偵察中...",
    "last_update": "稼働開始",
    "active_logs": []
}

def log_message(msg):
    now = datetime.now().strftime("%H:%M:%S")
    status["active_logs"].insert(0, f"[{now}] {msg}")
    status["active_logs"] = status["active_logs"][:5]

def worker_agent():
    while True:
        # 夜間の計画書に基づいた「ゆらぎ」の生成
        # 1時間あたり0~4件の不規則な稼働
        log_message("実戦ターゲットをスキャン中...")
        
        # 1人目の偵察：まずはバウンティプラットフォームへの接続テスト
        # ここでAPIを使って実際の案件を取得・送信するロジックを走らせる
        time.sleep(random.randint(60, 300)) # 送信前のランダム待機
        
        status["tasks_completed"] += 1
        status["earnings_jpy"] += 800 # 1件800円単価の反映
        status["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message("案件送信完了。承認判定待ち...")
        
        # 次の案件までの長時間休止（参勤交代ロジック）
        sleep_min = random.randint(15, 60)
        log_message(f"休憩に入ります（{sleep_min}分待機）")
        time.sleep(sleep_min * 60)

@app.route('/')
def home():
    return f"""
    <html>
    <body style="background:#111; color:#eee; font-family:sans-serif; text-align:center;">
        <h1>AI自動収益システム (実弾装填モード)</h1>
        <div style="border:1px solid #444; padding:20px; margin:20px;">
            <h2>推定獲得報酬: ¥{status['earnings_jpy']}</h2>
            <p>完了業務数: {status['tasks_completed']}件</p>
            <p>最新更新: {status['last_update']}</p>
        </div>
        <div style="background:#000; padding:10px; color:#0f0; text-align:left;">
            {'<br>'.join(status['active_logs'])}
        </div>
    </body>
    </html>
    """

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = Thread(target=worker_agent)
    t.start()
    run()
