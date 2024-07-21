import os
import shutil
import pathlib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox as msgbox

os.chdir(os.path.dirname(__file__))


def clear_logs():
    log_path = "../logs/"
    files = os.listdir(log_path)
    for file in files:
        file_path = os.path.join(log_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path}")
    print("All log files have been deleted.")
    msgbox.showinfo("Info", "All log files have been deleted.")


def clear_caches():
    cache_path = pathlib.Path("../../")
    files = list(cache_path.rglob("__pycache__"))
    if len(files) != 0:
        for dir in files:
            shutil.rmtree(dir)
        print("All cache files have been deleted.")
    else:
        print("Cache files not found.")
    msgbox.showinfo("Info", "All cache files have been deleted.")


def clear_profiles():
    result = msgbox.askyesno(
        "Warning",
        "OK to clear all profiles?",
        icon="warning")
    if result:
        with open("../data/theme.json", "w", encoding="utf-8") as f:
            f.write("{\"theme\": \"cosmo\"}")
            print("Rewrited theme.json")
        os.remove("../data/translator.appid.json")
        print("Deleted translator.appid.json")
        clear_logs()
        print("Deleted all log files")
        clear_caches()
        print("Deleted all cache files")
        msgbox.showinfo("Info", "All profiles have been cleared.")


def main():
    root = ttk.Window(themename="cosmo")
    root.title("Clear")
    root.geometry("350x300")
    root.resizable(False, False)
    title_label = ttk.Label(root, text="Clear", font=("Arial", 20, "bold"))
    clear_log = ttk.Button(
        root,
        text="Delete Log Files",
        command=clear_logs,
        bootstyle="primary-outline")
    clear_cache = ttk.Button(
        root,
        text="Delete Cache Files",
        command=clear_caches,
        bootstyle="primary-outline")
    clear_profile = ttk.Button(
        root,
        text="Erase All Profiles (DANGER)",
        command=clear_profiles,
        bootstyle="danger-outline")
    title_label.pack(pady=20)
    clear_log.pack(pady=10)
    clear_cache.pack(pady=10)
    clear_profile.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()
