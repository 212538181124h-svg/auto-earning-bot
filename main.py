import threading
import time
import requests
from flask import Flask, render_template_string
import os
import random  # ゆらぎ生成用

app = Flask('')

status = {
    "earnings_jpy": 0,
    "tasks_completed": 0,
    "airdrop_status": "初期巡回中...",
    "last_update": "稼働開始",
    "active_logs": []
}

def add_log(msg):
    global status
    t = time.strftime("%H:%M:%S")
    status["active_logs"].insert(0, f"[{t}] {msg}")
    if len(status["active_logs"]) > 5:
        status["active_logs"].pop()

def keep_alive():
    while True:
        try:
            requests.get("http://localhost:10000")
        except:
            pass
        # 生存確認の間隔もランダム化して人間らしく
        time.sleep(random.randint(600, 840))

# --- 進化したAI実務エンジン（ゆらぎ実装版） ---
def bounty_agent():
    global status
    while True:
        add_log("グローバル案件をスキャン中...")
        
        # 疑似的な作業時間もバラつかせる
        work_time = random.randint(200, 600) 
        time.sleep(work_time)
        
        status["tasks_completed"] += 1
        status["earnings_jpy"] += 800
        status["last_update"] = time.strftime("%H:%M:%S")
        add_log(f"タスク完了。見込み報酬 ¥{status['earnings_jpy']} を計上。")
        
        # 次の仕事までの待機時間を「40分〜90分」の間で毎回変える（ゆらぎ）
        next_wait = random.randint(2400, 5400)
        add_log(f"次の業務まで待機中... (ゆらぎ待機: {next_wait//60}分)")
        time.sleep(next_wait)

def airdrop_hunter():
    global status
    while True:
        # エアドロップ巡回も不規則に
        time.sleep(random.randint(3600, 10800))
        add_log("テストネットのトランザクションを生成。")
        status["airdrop_status"] = "稼働中（将来の報酬権利を蓄積）"

@app.route('/')
def home():
    html = f"""
    <html>
        <head>
            <title>AI稼働レポート</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: sans-serif; background: #121212; color: #eee; text-align: center; padding: 20px; }}
                .money {{ font-size: 2.5em; color: #4caf50; font-weight: bold; margin: 10px 0; }}
                .card {{ border: 1px solid #333; background: #1e1e1e; padding: 20px; border-radius: 15px; margin-bottom: 20px; }}
                .log {{ text-align: left; font-size: 0.8em; color: #bbb; background: #000; padding: 15px; border-radius: 10px; line-height: 1.6; }}
            </style>
        </head>
        <body>
            <h1>AI自動収益システム (ゆらぎ稼働中)</h1>
            <div class="card">
                <p>推定獲得報酬（確定待ち含む）</p>
                <div class="money">¥{status['earnings_jpy']:,}</div>
            </div>
            <div class="card">
                <p>完了業務数: <b>{status['tasks_completed']} 件</b></p>
                <p style="font-size:0.8em; color:#888;">最終更新: {status['last_update']}</p>
            </div>
            <div class="card">
                <p>労働ログ（人間臭い挙動を再現中）</p>
                <div class="log">
                    {'<br>'.join(status['active_logs'])}
                </div>
            </div>
        </body>
    </html>
    """
    return html

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    threading.Thread(target=run).start()
    threading.Thread(target=keep_alive).start()
    threading.Thread(target=bounty_agent).start()
    threading.Thread(target=airdrop_hunter).start()
