import tkinter as tk
import os
from dotenv import load_dotenv
from urllib.parse import urljoin

from browser.session import start_browser
from actions.login import login
from actions.fillevent import fill_event
from actions.order_read import get_order_summary

load_dotenv()

page = None

def run_script():

    global page
    
    base_url = os.getenv("STAGE")

    # 抓.env帳密
    username = os.getenv("FSKYUSERNAME")
    password = os.getenv("FSKYPASSWORD")

    page = start_browser(base_url)

    login(page, username, password)


root = tk.Tk()

# stage變數設定
selected_stage = tk.StringVar(value="stage")

# 建GUI
tk.Label(root, text="Select Stage").pack(pady=10)


    # training = page.get_by_text("Training")
    # training.wait_for()
    # training.click()

    # event_url = urljoin(base_url, "bos/#/events")

    # page.goto(
    #     event_url,
    #     wait_until="domcontentloaded"
    # )

    # input("Press Enter to exit")


stages = ["stage",
         "stage2",
         "stage3",
         "stage4",
         "stage5"]

for s in stages:
    tk.Button(
        root,
        text=s,
        width=15,
        command=lambda stage=s: set_stage(stage),
        # command=lambda stage=s: run_script(stage),
    ).pack(pady=2)

tk.Button(
    root,
    text="Start",
    width=15,
    command=run_script
).pack(pady=2)

tk.Button(
    root,
    text="Fill Event",
    command=fill_event
).pack()
    
root.mainloop()