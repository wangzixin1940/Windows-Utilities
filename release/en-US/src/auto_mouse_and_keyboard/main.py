import ttkbootstrap as ttk
import tkinter.filedialog as fdg
import tkinter.messagebox as msgbox
import traceback
import pynput
from pynput import mouse
from pynput import keyboard
from time import sleep as delay
from random import randint as rand


class Controllers:
    def __init(self):
        self.mouse = mouse.Controller()
        self.keybrd = keyboard.Controller()


class Functions:
    def __init__(self):
        self.mouse = pynput.mouse
        self.keybrd = pynput.keyboard

    @staticmethod
    def delay(*args, **kwargs):
        return delay(*args, **kwargs)

    @staticmethod
    def rand(*args, **kwargs):
        return rand(*args, **kwargs)


Controllers = Controllers()
Functions = Functions()

# Available methods: mouse, keyboard, delay, rand

# mouse, keybrd grammar see https://pynput.readthedocs.io/en/latest/index.html

# delay grammar:
# delay(sec: int)
# Wait sec seconds

# rand grammar:
# rand(min: int, max: int)
# Take a random number between min and max

mouse = mouse.Controller()
keyboard = keyboard.Controller()


class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Auto Mouse and Keyboard")
        self.geometry("400x300")
        self.resizable(False, False)
        self.main_title = ttk.Label(
            self, text="Auto Mouse and Keyboard", font=(
                "Arial", 20))
        self.file = ttk.StringVar(value="Open File")
        self.input_file = ttk.Button(
            self,
            textvariable=self.file,
            command=self.open_file,
            width=15,
            bootstyle="primary-outline")
        self.do_work_btn = ttk.Button(
            self,
            text="RUN",
            command=self.do_work,
            width=15,
            bootstyle="success-outline")
        self.main_title.pack(pady=20)
        self.input_file.pack(pady=10)
        self.do_work_btn.pack(pady=10)
        self.mainloop()

    def open_file(self):
        self.file.set(
            fdg.askopenfilename(
                title="Open...", filetypes=[
                    ("AMK Script", "*.amk"), ("Python Script", "*.py")]))

    def do_work(self):
        if self.file.get() != "Open File":
            with open(self.file.get(), "r", encoding="utf-8") as f:
                data = f.read()
                if (data.startswith("#-- ENABLE --#")):
                    try:
                        exec(data)
                    except Exception as e:
                        msgbox.showerror(
                            "Error", f"An error occurred while executing the script: \n{
                                repr(e)}：\n{
                                traceback.print_exc()}")
                else:
                    msgbox.showerror(
                        "Error", "Script is disabled!\nPlease add at the beginning of the script: \n#-- ENABLE --#\n. Or replace #-- DISABLE --# with #-- ENABLE --#")
        else:
            msgbox.showerror("Error", "Please select the file first!")


if __name__ == "__main__":
    App()
