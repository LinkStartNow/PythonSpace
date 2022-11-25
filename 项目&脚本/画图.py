''' ��ͼ '''

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *

siz_w = 600  # �����Ŀ��
siz_h = 400  # �����ĸ߶�

class Paint(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.x = 0; self.y = 0  # ��ͼ��ʼ������
        self.bgcolor = '#ff0000'  # �ʴ���ɫ��Ĭ�Ϻ�ɫ
        self.lastdraw = 0  # �����һ�������ߣ�����ɾ��
        self.drawing = False  # ��ʼ�滭�ı�ǣ�����ȷ����ʼ��
        self.fillcolor = ''  # �����ɫ��Ĭ����
        self.eraser_siz = 4
        self.back = '#ffffff'
        self.pack()
        self.cre()

    def cre(self):
        # ������ͼ����
        self.drawpad = Canvas(self, bg='white', width=siz_w, height=siz_h)
        self.drawpad.pack()

        # �����Ҽ����ز˵�
        self.menu = Menu(self.drawpad)  # �Ѳ˵����ڻ�����
        self.menu.add_command(label='����������ɫ', command=self.changecolor)
        self.menu.add_command(label='����������ɫ', command=self.changebg)
        self.menu.add_command(label='���������ɫ', command=self.chfill)
        self.menu.add_command(label='���������ɫ', command=self.chout)

        # ��Ƥ��Сѡ��
        self.siz = Scale(self.drawpad, from_=1, to=10, tickinterval=2, command=self.siz_ch, orient=HORIZONTAL)

        # ������ť
        pd = 5  # ��ť���
        bt_pen = Button(self, text='����', name='pen')  # Ϊ��ť�������֣��������
        bt_pen.pack(side='left', padx=pd)
        bt_rect = Button(self, text='����', name='rect')
        bt_rect.pack(side='left', padx=pd)
        bt_line = Button(self, text='ֱ��', name='line')
        bt_line.pack(side='left', padx=pd)
        bt_line_arrow = Button(self, text='����ͷ��ֱ��', name='arrow')
        bt_line_arrow.pack(side='left', padx=pd)
        bt_eraser = Button(self, text='��Ƥ', name='eraser')
        bt_eraser.pack(side='left', padx=pd)
        bt_clear = Button(self, text='����', name='clear')
        bt_clear.pack(side='left', padx=pd)
        bt_quit = Button(self, text='�˳�', name='quit')
        bt_quit.pack(side='left', padx=pd)

        bt_eraser.bind('<3>', self.siz_eraser)
        bt_rect.bind_class('Button', '<1>', self.EventManager)  # ����������࣬��ΰ�
        self.drawpad.bind('<ButtonRelease-1>', self.stop_draw)  # Ϊ������ͷ�����¼�
        self.drawpad.bind('<3>', self.cre_menu)  # Ϊ������Ҽ������¼����ٻ����ز˵�
        self.drawpad.bind('<1>', lambda event : self.siz.place_forget())

        # ��ݼ�������ɫ
        root.bind('<KeyPress-g>', self.quick)
        root.bind('<KeyPress-r>', self.quick)
        root.bind('<KeyPress-b>', self.quick)
        root.bind('<KeyPress-y>', self.quick)

    def EventManager(self, event):
        ''' �������а�ť�������¼� '''
        self.siz.place_forget()
        name = event.widget.winfo_name()  # ��ѯ�����¼���Ԫ�������֣��ҵ�������İ�ť
        # print(name)
        if name == 'line':
            self.drawpad.bind('<B1-Motion>', self.my_line)  # ÿ�ζ�����Ϊ����϶����µĺ������Ա����л�ģʽ
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
        ''' �������λ�õ��Աߴ������ز˵� '''
        self.menu.post(event.x_root, event.y_root)

    def chfill(self):
        ''' �������ɫ '''
        self.fillcolor = askcolor()[1]

    def changecolor(self):
        ''' �ıʴ���ɫ '''
        self.bgcolor = askcolor()[1]

    def chout(self):
        ''' ����߿���ɫ '''
        self.bgcolor = askcolor()[1]

    def changebg(self):
        ''' �Ļ�����ɫ '''
        self.back = askcolor()[1]
        self.drawpad.config(bg=self.back)

    def siz_eraser(self, event):
        ''' ������Ƥ��Сѡ�񻬿� '''
        # xx = event.widget.winfo_x(); yy = event.widget.winfo_y()
        xx = 250; yy = 330
        self.siz.place(x=xx, y=yy)

    def siz_ch(self, sy):
        self.eraser_siz = int(sy)

    def my_eraser(self, event):
        ''' ��Ƥ '''
        self.drawpad.create_rectangle(event.x - self.eraser_siz, event.y - self.eraser_siz, event.x + self.eraser_siz, event.y + self.eraser_siz, fill=self.back, outline='')

    def my_pen(self, event):
        ''' ���ʹ��� '''
        self.start_draw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor)
        self.x = event.x; self.y = event.y

    def rec(self, event):
        ''' �����εĺ��� '''
        self.start_draw(event)
        self.lastdraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.bgcolor, fill=self.fillcolor)
        #                                                                                    ��߿���ɫ

    def stop_draw(self, event):
        ''' ͣ�ʴ����ĺ��� '''
        self.drawing = False
        self.lastdraw = 0  # ����󻭵�����գ���ֹ�´λ�ʱɾ���������

    def start_draw(self, event):
        ''' ��ʼ��ͼ�ĳ�ʼ�� '''
        if not self.drawing:
            self.drawing = True
            self.x = event.x; self.y = event.y  # ��ʼ��ֱ��ʱ��¼����㣬���߹����й��㲻�ٱ䶯���
        self.drawpad.delete(self.lastdraw)  # ɾ����һ�λ滭

    def my_line(self, event):
        ''' ��ֱ�ߵĺ��� '''
        self.start_draw(event)  # ��ͷ��ֱ�ߵĳ�ʼ����ͬ�����԰���һ�𣬼��ٴ���
        self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor)
        #  �����ڻ����߸�ֵ�����һ�λ��߱���             �ߵ���ʼ��          �ߵ��յ�         �����ɫ

    def my_line_arrow(self, event):
        ''' ������ͷֱ�ߵĺ��� '''
        self.start_draw(event)
        self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.bgcolor, arrow=LAST)
        #                                                                                             ��ͷ����λ��


root = Tk()
# root.geometry('400x300+100+100')
root.title('Paint')
app = Paint(root)
root.mainloop()