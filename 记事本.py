''' 记事本功能完善版 '''
'''
    打包成.exe文件:
        1.在终端（Terminal）下找到文件的路径
        2.pyinstaller -F 要打包的文件.py
        3.最后会生成一个dist文件夹，exe文件就在里面
'''

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *

class notepade(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.cre()

    def cre(self):
        menuroot = Menu(root)

        menuFile = Menu(menuroot)
        menuEdit = Menu(menuroot)
        menuHelp = Menu(menuroot)

        menuroot.add_cascade(label='文件(F)', menu=menuFile)
        menuroot.add_cascade(label='编辑(E)', menu=menuEdit)
        menuroot.add_cascade(label='帮助(H)', menu=menuHelp)

        menuFile.add_command(label='新建', accelerator='Ctrl+n', command=self.newfile)
        menuFile.add_command(label='打开', accelerator='Ctrl+o', command=self.openfile)
        menuFile.add_command(label='保存', accelerator='Ctrl+s', command=self.savefile)
        menuFile.add_separator()
        menuFile.add_command(label='退出', accelerator='Ctrl+q', command=self.quit)

        self.tex = Text(root)
        self.tex.pack()

        self.rightmenu = Menu(root)
        self.rightmenu.add_command(label='换背景色', command=self.colorback)
        self.rightmenu.add_command(label='换字体颜色', command=self.colorfont)


        root.bind('<Button-3>', self.right)

        # 快捷键设置
        root.bind('<Control-n>', lambda event : self.newfile())
        root.bind('<Control-s>', lambda event: self.savefile())
        root.bind('<Control-o>', lambda event: self.openfile())
        root.bind('<Control-q>', lambda event: self.quit())

        root['menu'] = menuroot

    def right(self, event):
        self.rightmenu.post(event.x_root, event.y_root)

    def savefile(self):
        with open(self.filename, 'w') as f:
            c = self.tex.get(1.0, END)
            f.write(c)

    def newfile(self):
        self.tex.delete(1.0, END)
        self.filename = asksaveasfilename(title='另存为', initialfile='1.txt',
                                          filetypes=[('文本文件', '*.txt')],
                                          defaultextension='.txt')
        self.savefile()
        root.title(self.filename.split('/')[-1])


    def openfile(self):
        self.tex.delete(1.0, END)  # 打开前先清空文本框
        with askopenfile(title='打开文件',
                         initialdir='e:') as f:
            self.tex.insert(INSERT, f.read())
            self.filename = f.name  # 存下打开的文件的名字
            root.title(f.name.split('/')[1])  # 修改窗口名称，方便了解目前打开的文件名

    def colorback(self):
        color = askcolor(title='选取要更换的背景颜色')
        self.tex.config(bg=color[1])  # 修改背景颜色

    def colorfont(self):
        color = askcolor(title='选取要更换的背景颜色')
        self.tex.config(fg=color[1])  # 修改前景色也就是修改字体颜色

    def quit(self):
        root.quit()


root = Tk()
root.geometry('400x300+100+100')
root.title('NotePad')
app = notepade(root)
root.mainloop()