import tkinter as tk

def run_script():
    username = entry_user.get()
    password = entry_pass.get()
    print(username, password)

root = tk.Tk()

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Start", command=run_script).pack()

root.mainloop()