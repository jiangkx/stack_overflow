from tkinter import *
from tkinter import scrolledtext
import csv

def main():
    filepath = "C:/spider/export.csv"
    global keyword, text, num, k1
    # 创建空白窗口,作为主载体
    root = Tk()
    root.title('Stack Overflow Spider')

    # 窗口的大小，后面的加号是窗口在整个屏幕的位置
    root.geometry('1050x625+198+79')

    # 标签控件，窗口中放置文本组件
    Label(root, text='输入爬取关键词（多个请用+隔开，不要有空格）:', font=("华文行楷", 20), fg='black').grid(row=0, column=0, sticky=W)

    # 定位 pack包 place位置 grid是网格式的布局 #Entry是可输入文本框
    keyword = Entry(root, font=("微软雅黑", 15))
    keyword.grid(row=1, column=0)

    Label(root, text='输入爬取问题的数量:', font=("华文行楷", 20), fg='black').grid(row=2, column=0, sticky=W)
    k1 = Entry(root, font=("微软雅黑", 15))
    k1.grid(row=3, column=0)
    #可优化（同时含有以空格间隔，或含有用+间隔）
    Label(root, text='可对问题再次选取，问题中应含有的关键字:', font=("华文行楷", 20), fg='black').grid(row=8, column=0,sticky=W)
    k2 = Entry(root, font=("微软雅黑", 15))
    k2.grid(row=9, column=0)
    Label(root, text='定制功能（可选）:', font=("华文行楷", 20), fg='black').grid(row=5, column=0, sticky=W)
    Label(root, text='完成爬取后点击对数据进行查看', font=("华文行楷", 20), fg='black').grid(row=6, column=0, sticky=W)

    def shuju():
        filepath = "C:/spider/export.csv"
        root1 = Tk()
        root1.title('数据')
        root1.geometry('850x325+220+100')

        sda = scrolledtext.ScrolledText(root1, width=120, height=20, font=("宋体", 12), fg='black', relief="solid")
        sda.grid(row=0, column=0, sticky=W)
        with open(filepath, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for i in reader:
                try:
                    print(i[0])
                    sda.insert(END, i[3]+' ')
                    sda.insert(END, i[0]+ '\n\n')

                except:
                    continue

    # 列表控件
    #text = Listbox(root, font=('微软雅黑', 15), width=45, height=10)

    # columnspan 组件所跨越的列数
    # text.grid(row=1, columnspan=2)

    # 设置按钮 sticky对齐方式，N S W E
    # 开始爬取按钮后还缺少 command 跳转至爬虫解析函数
    button = Button(root, text='开始爬取', font=("微软雅黑", 15)).grid(row=4, column=0, sticky=W)
    button = Button(root, text='数据查看', font=("微软雅黑", 15),command=shuju()).grid(row=7, column=0, sticky=W)
    button = Button(root, text='退出工具', font=("微软雅黑", 15), command=root.quit).grid(row=4, column=1, sticky=E)
    button = Button(root, text='数据选择', font=("微软雅黑", 15)).grid(row=10, column=0, sticky=W)

    # 使得窗口一直存在
    mainloop()

main()