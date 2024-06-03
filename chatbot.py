# chatbot.py

import tkinter as tk
from tkinter import scrolledtext
from model import ChatBotModel

# モデルを初期化
chatbot_model = ChatBotModel()


# ボタンがクリックされたときに呼ばれる関数
def send_message():
    user_input = user_entry.get()
    if user_input:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "あなた: " + user_input + "\n")
        chat_window.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

        # AIからの応答を生成
        response = chatbot_model.generate_response(user_input)

        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "AI: " + response + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)


# メインウィンドウの設定
root = tk.Tk()
root.title("AIチャットボット")

# スクロール可能なテキストウィジェット
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# エントリーウィジェット
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=10, fill=tk.X)

# 送信ボタン
send_button = tk.Button(root, text="送信", command=send_message)
send_button.pack(pady=10)

# GUIのメインループ
root.mainloop()

#python chatbot.py
#↑これで実行