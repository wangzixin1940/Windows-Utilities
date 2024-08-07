from tkinter import messagebox as msgbox
from tkinter import filedialog as fdg
import ttkbootstrap as ttk
from PIL import Image
import os
os.chdir(os.path.dirname(__file__))
# 更换工作目录


class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Photo Format Converter")
        self.geometry("450x300")
        self.resizable(False, False)
        self.style_set = ttk.Style()
        self.style_set.theme_use("cosmo")
        self.style_set.configure("TButton", font=("Arial", 12), width=20)
        self.iconbitmap("assets/favicon.ico")
        # 创建控件
        self.main_title = ttk.Label(
            self, text="Photo Format Converter", font=(
                "Arial", 20))
        self.main_title.pack(pady=10)
        self.image_path = ttk.StringVar(value="请选择图片")
        self.input_button = ttk.Button(
            self, textvariable=self.image_path, command=self.open_file)
        self.input_button.pack(pady=10)
        self.convert_button = ttk.Button(self, text="转换", command=self.convert)
        self.convert_button.pack(pady=10)
        # 主循环
        self.mainloop()

    def open_file(self):
        file_path = fdg.askopenfilename(
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            self.image_path.set(file_path)

    def convert(self):
        if self.image_path.get() == "请选择图片":
            msgbox.showwarning("警告", "请先选择图片！")
            return
        image = Image.open(self.image_path.get())
        output = fdg.asksaveasfilename(
            defaultextension=".jpg", filetypes=[
                ("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp"), ("GIF", "*.gif")])
        if output:
            image.save(output)
            msgbox.showinfo("提示", "转换成功！")
            return


if __name__ == "__main__":
    App()
