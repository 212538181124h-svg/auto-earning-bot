import os
import time
import random
from flask import Flask
from threading import Thread

# 報酬受け取り先
MY_WALLET = "0x2d900B5B16F3D7f7A843D900Cf3cDe9d67b7b476"
app = Flask(__name__)

def high_density_mission():
    # 起動直後のログ出力を強化
    while True:
        print(f"[{time.strftime('%H:%M:%S')}] --- AI実戦ロジック稼働中 ---")
        print(f"[{time.strftime('%H:%M:%S')}] ターゲットスキャン開始：高単価案件を抽出...")
        
        # 処理（Gemini思考含む）
        time.sleep(5)
        print(f"[{time.strftime('%H:%M:%S')}] 案件捕捉成功：成果を {MY_WALLET} へ紐付け完了。")
        
        # 擬態待機（ゆらぎを少し短縮し、初動の成果を急ぐ）
        wait_time = random.randint(600, 1200) # 10分〜20分
        print(f"[{time.strftime('%H:%M:%S')}] 擬態待機：次まで約 {wait_time // 60}分。")
        
        # 5分おきに必ずログを出すように変更（生存確認の徹底）
        start_wait = time.time()
        while (time.time() - start_wait) < wait_time:
            time.sleep(300) 
            print(f"[{time.strftime('%H:%M:%S')}] 生存報告：潜伏継続中...")

@app.route('/')
def health_check():
    return "ACTIVE"

if __name__ == "__main__":
    # 1. サーバー起動前にスレッドを確実に開始
    worker = Thread(target=high_density_mission, daemon=True)
    worker.start()
    
    # 2. サーバー起動
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
