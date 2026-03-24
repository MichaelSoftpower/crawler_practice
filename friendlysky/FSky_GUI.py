import tkinter as tk
import os
from dotenv import load_dotenv
from urllib.parse import urljoin

load_dotenv()

# 抓.env帳密
username = os.getenv("FSKYUSERNAME")
password = os.getenv("FSKYPASSWORD")

def get_stage_url(stage):
    return os.getenv(stage.upper())

def set_stage(stage):
    selected_stage.set(stage)


root = tk.Tk()

# stage變數設定
selected_stage = tk.StringVar(value="stage")

# 建GUI
tk.Label(root, text="Select Stage").pack(pady=10)

def run_script():
    stage = selected_stage.get()
    base_url = get_stage_url(stage)
    if not base_url:
        return

    training = page.get_by_text("Training")
    training.wait_for()
    training.click()

    event_url = urljoin(base_url, "bos/#/events")

    page.goto(
        event_url,
        wait_until="domcontentloaded"
    )

    # input("Press Enter to exit")

def fill_event():
    global page

    # for Playwright Inspector
    # page.pause()

    if page is None:
        print("Browser not started")
        return

    page.locator("input[placeholder='title']").fill(
        "First Parth 2026"
    )

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