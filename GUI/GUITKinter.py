from tkinter import filedialog
from tkinter import *


class ImgView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Select Image_ChoiYoungHyo")
        self.window.geometry("700x500")
        self.window.resizable(True, True)

        self.menubar = Menu(self.window)
        menu_1 = Menu(self.menubar, tearoff=0)
        menu_1.add_command(label="open", command=self.folderSelect)
        menu_1.add_separator()

        menu_1.add_command(label="exit", command=self.close)
        self.menubar.add_cascade(label="file", menu=menu_1)
        self.window.config(menu=self.menubar)

        self.window.mainloop()

    def folderSelect(self):
        path = filedialog.askdirectory()
        print(path)
        return path

    def close(self):
        self.window.quit()
        self.window.destroy()


a = ImgView()