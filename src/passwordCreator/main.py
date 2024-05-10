import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 更换编码

import os
os.chdir(os.path.dirname(__file__))
# 更换工作目录


import logging
import datetime
import random
import ttkbootstrap as ttk
from tkinter import messagebox as msgbox


logging.basicConfig(
                filename=f"../../logs/{datetime.date.today()}.log",
                level=logging.INFO,
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("PWDCTR")


def passwordCreator(length:int, includeSymbols:bool=False, includeNumbers:bool=True, includeUppercase:bool=True):
        """
        length: 密码长度
        includeSymbols: 是否包含符号
        includeNumbers: 是否包含数字
        includeUppercase: 是否包含大写字母
        return: 返回密码字符串
        """
        # 密码字符集
        chars = {"lowers":"abcdefghijklmnopqrstuvwxyz", "uppers":"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "numbers":"0123456789", "symbols":r"!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"}
        if not includeSymbols: del chars["symbols"]
        if not includeNumbers: del chars["numbers"]
        if not includeUppercase: del chars["uppers"]
        password = ""
        try :
            for i in range(int(length)):
                # 随机选择一个字符集
                charset = random.choice(list(chars.keys()))
                # 随机选择一个字符
                char = random.choice(chars[charset])
                # 添加到密码字符串
                password += char
            return password
        except KeyError as err:
            logger.error(f"KEY ERROR: {err}")
            return 1
        except Exception as err:
            logger.error(f"ERROR: {err}")
            raise err


def main():
    def changeValue():
        password.config(state="normal")
        password.delete("1.0", "end")
        password.insert("1.0", passwordCreator(length.get(), includeSymbols.get(), includeNumbers.get(), includeUppercase.get()))
        password.config(state="disabled")

    root = ttk.Window("Password Creator", "cosmo")
    root.geometry("400x400")
    root.resizable(False, False)
    root.iconbitmap("./assets/icon.ico")
    root.title("Password Creator")
    title = ttk.Label(root, text="Password Creator", font=("Arial", 20))
    title.pack(pady=10)
    length = ttk.Spinbox(root, from_=4, to=32, width=10)
    length.pack(pady=5)
    includeSymbols = ttk.BooleanVar(value=True)
    includeNumbers = ttk.BooleanVar(value=True)
    includeUppercase = ttk.BooleanVar(value=True)
    symbols = ttk.Checkbutton(root, text="Symbols", variable=includeSymbols)
    numbers = ttk.Checkbutton(root, text="Numbers", variable=includeNumbers)
    uppercase = ttk.Checkbutton(root, text="Uppercase", variable=includeUppercase)
    symbols.pack(pady=5)
    numbers.pack(pady=5)
    uppercase.pack(pady=5)
    generate = ttk.Button(root, text="Generate", command=lambda:changeValue())
    generate.pack(pady=10)
    password = ttk.Text(root, width=30, height=5)
    password.config(state="disabled")
    password.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()