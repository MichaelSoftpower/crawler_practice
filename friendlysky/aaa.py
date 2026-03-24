import tkinter as tk
from playwright.sync_api import sync_playwright

# 用來記住目前選擇的 stage
selected_stage = tk.StringVar(value="stage1")


def set_stage(stage_name):
    selected_stage.set(stage_name)
    print(f"Selected: {stage_name}")


def run_script():
    stage = selected_stage.get()
    url = f"https://{stage}.fky.com/"

    print(f"Opening: {url}")

    with sync_playwright() as p:
        print("Starting browser...")

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()
        page.goto(
            url,
            wait_until="domcontentloaded"
        )


root = tk.Tk()
root.title("Stage Selector")

tk.Label(root, text="Select Stage").pack(pady=10)

# 建立 stage1 ~ stage5 buttons
for i in range(1, 6):
    stage_name = f"stage{i}"
    tk.Button(
        root,
        text=stage_name,
        width=15,
        command=lambda s=stage_name: set_stage(s)
    ).pack(pady=2)

tk.Button(
    root,
    text="Start",
    width=15,
    command=run_script
).pack(pady=20)

root.mainloop()