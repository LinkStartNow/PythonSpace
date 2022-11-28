''' 画图 '''

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *

siz_w = 600  # 画布的宽度
siz_h = 400  # 画布的高度

class Paint(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.x = 0; self.y = 0  # 画图起始点坐标
        self.bgcolor = '#ff0000'  # 笔触颜色，默认红色
        self.lastdraw = 0  # 标记上一条画的线，便于删除
        self.drawing = False  # 开始绘画的标记，用于确定起始点
        self.fillcolor = ''  # 填充颜色，默认无
        self.eraser_siz = 4
        self.back = '#ffffff'
        self.pack()
        self.cre()

    def cre(self):
        # 创建绘图区域
        self.drawpad = Canvas(self, bg='white', width=siz_w, height=siz_h)
        self.drawpad.pack()

        # 创建右键隐藏菜单
        self.menu = Menu(self.drawpad)  # 把菜单绑定在画板上
        self.menu.add_command(label='更换换笔颜色', command=self.changecolor)
        self.menu.add_command(label='更换画板颜色', command=self.changebg)
        self.menu.add_command(label='更换填充颜色', command=self.chfill)
        self.menu.add_command(label='更换外框颜色', command=self.chout)

        # 橡皮大小选择
        self.siz = Scale(self.drawpad, from_=1, to=10, tickinterval=2, command=self.siz_ch, orient=HORIZONTAL)

        # 创建按钮
        pd = 5  # 按钮间距
        bt_pen = Button(self, text='画笔', name='pen')  # 为按钮设置名字，方便管理
        bt_pen.pack(side='left', padx=pd)
        bt_rect = Button(self, text='矩形', name='rect')
        bt_rect.pack(side='left', padx=pd)
        bt_line = Button(self, text='直线', name='line')
        bt_line.pack(side='left', padx=pd)
        bt_line_arrow = Button(self, text='带箭头的直线', name='arrow')
        bt_line_arrow.pack(side='left', padx=pd)
        bt_eraser = Button(self, text='橡皮', name='eraser')
        bt_eraser.pack(side='left', padx=pd)
        bt_clear = Button(self, text='清屏', name='clear')
        bt_clear.pack(side='left', padx=pd)
        bt_quit = Button(self, text='退出', name='quit')
        bt_quit.pack(side='left', padx=pd)

        bt_eraser.bind('<3>', self.siz_eraser)
        bt_rect.bind_class('Button', '<1>', self.EventManager)  # 避免代码冗余，多次绑定
        self.drawpad.bind('<ButtonRelease-1>', self.stop_draw)  # 为画板绑定释放鼠标事件
        self.drawpad.bind('<3>', self.cre_menu)  # 为画板绑定右键单击事件，召唤隐藏菜单
        self.drawpad.bind('<1>', lambda event : self.siz.place_forget())

        # 快捷键更换颜色
        root.bind('<KeyPress-g>', self.quick)
        root.bind('<KeyPress-r>', self.quick)
        root.bind('<KeyPress-b>', self.quick)
        root.bind('<KeyPress-y>', self.quick)

    def EventManager(self, event):
        ''' 管理所有按钮触发的事件 '''
        self.siz.place_forget()
        name = event.widget.winfo_name()  # 查询触发事件的元件的名字，找到被点击的按钮
        # print(name)
        if name == 'line':
            self.drawpad.bind('<B1-Motion>', self.my_line)  # 每次都重新为鼠标拖动绑定新的函数，以便于切换模式
        elif name == 'arrow':
            self.drawpad.bind('<B1-Motion>', self.my_line_arrow)
        elif name == 'rect':
            self.drawpad.bind('<B1-Motion>', self.rec)
        elif name == 'pen':
            self.drawpad.bind('<B1-Motion>', self.my_pen)
        elif name == 'quit':
            root.quit()
        elif name == 'eraser':
            self.drawpad.bind('<B1-Motion>', self.my_eraser)
        elif name == 'clear':
            self.drawpad.delete('all')

    def quick(self, event):
        if event.char == 'g':
            self.bgcolor = '#00ff00'
        elif event.char == 'r':
            self.bgcolor = '#ff0000'
        elif event.char == 'y':
            self.bgcolor = '#ffff00'
        elif event.char == 'b':
            self.bgcolor = '#0000ff'


    def cre_menu(self, event):
        ''' 在鼠标点击位置的旁边创建隐藏菜单 '''
        self.menu.post(event.x_root, event.y_root)

    def chfill(self):
        ''' 改填充颜色 '''
        self.fillcolor = askcolor()[1]

    def changecolor(self):
        ''' 改笔触颜色 '''
        self.bgcolor = askcolor()[1]

    def chout(self):
        ''' 改外边框颜色 '''
        self.bgcolor = askcolor()[1]

    def changebg(self):
        ''' 改画板颜色 '''
        self.back = askcolor()[1]
        self.drawpad.config(bg=self.back)

    def siz_eraser(self, event):
        ''' 创建橡皮大小选择滑块 '''
        # xx = event.widget.winfo_x(); yy = event.widget.winfo_y()
        xx = 250; yy = 330
        self.siz.place(x=xx, y=yy)

    def siz_ch(self, sy):
        self.eraser_siz = int(sy)

    def my_eraser(self, event):
        ''' 橡皮 '''
        self.drawpad.create_rectangle(event.x - self.eraser_siz, event.y - self.eraser_siz, event.x + self.eraser_siz, event.y + self.eraser_siz, fill=self.back, outline='')

    def my_pen(self, event):
        ''' 画笔工具 '''
        self.start_draw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor)
        self.x = event.x; self.y = event.y

    def rec(self, event):
        ''' 画矩形的函数 '''
        self.start_draw(event)
        self.lastdraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.bgcolor, fill=self.fillcolor)
        #                                                                                    外边框颜色

    def stop_draw(self, event):
        ''' 停笔触发的函数 '''
        self.drawing = False
        self.lastdraw = 0  # 把最后画的线清空，防止下次画时删除画完的线

    def start_draw(self, event):
        ''' 开始画图的初始化 '''
        if not self.drawing:
            self.drawing = True
            self.x = event.x; self.y = event.y  # 开始画直线时记录下起点，画线过程中国便不再变动起点
        self.drawpad.delete(self.lastdraw)  # 删除上一次绘画

    def my_line(self, event):
        ''' 画直线的函数 '''
        self.start_draw(event)  # 箭头和直线的初始化相同，所以包在一起，减少代码
        self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor)
        #  把现在画的线赋值给最后一次划线变量             线的起始点          线的终点         填充颜色

    def my_line_arrow(self, event):
        ''' 画带箭头直线的函数 '''
        self.start_draw(event)
        self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor, arrow=LAST)
        #                                                                                             箭头放置位置


root = Tk()
# root.geometry('400x300+100+100')
root.title('Paint')
app = Paint(root)
root.mainloop()