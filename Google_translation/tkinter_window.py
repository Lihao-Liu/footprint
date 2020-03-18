'''
Run this file
This file contain the visual window and the main function
Author: Lihao Liu
2020.3.17
'''
import tkinter as tk
from spider import spider_translate

'''计算窗口居中的位置'''
def get_window_positon(width, height):
    sw = window.winfo_screenwidth()
    # 得到屏幕宽度
    sh = window.winfo_screenheight()
    # 得到屏幕高度
    window_x_position = (sw - width) // 2
    window_y_position = (sh - height) // 2
    return window_x_position, window_y_position
'''将文本传给翻译器'''
def traslating():
    in_text=in_.get("0.0","end")#获取输入文本框内容
    out_text,status_code=spider_translate(in_text)
    out_.delete(0.0 , tk.END)  # 删除所有值
    out_.insert (0.0, out_text )
    if status_code==200:
        foo="Succeed!"
        state.config(text=foo)
    else:
        foo = "Fail!"
        state.config(text=foo)
'''清空文本'''
def cleaning():
    out_.delete(0.0, tk.END)  # 删除所有值
    in_.delete(0.0, tk.END)  # 删除所有值
    foo = "Show state"
    state.config(text=foo)

if __name__ =='__main__':
    global tk,canvas
    window=tk.Tk()#窗口
    window.title('My Translator')
    # window.geometry('800x500')#长宽 长x宽
    tk_width = 800 # 窗口的宽度
    tk_height = 500 # 窗口的长度
    pos = get_window_positon(tk_width, tk_height) #调用get_window_positon()方法
    window.geometry(f'{tk_width}x{tk_height}+{pos[0]}+{pos[1]}') # 窗口的大小与位置
    window.resizable(False, False) # 窗口大小不可变
    '''文本框'''
    #输入
    #设置滚动条
    scroll = tk.Scrollbar()
    in_=tk.Text(window,width=45,height=35,bd=5)
    scroll.pack(side=tk.LEFT,fill=tk.Y) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    in_.pack(side=tk.LEFT,fill=tk.Y)
    scroll.config(command=in_.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    in_.config(yscrollcommand=scroll.set) # 将滚动条关联到文本框
    #输出
    scroll_1 = tk.Scrollbar()
    out_=tk.Text(window,width=45,height=35,bd=5)
    scroll_1.pack(side=tk.RIGHT,fill=tk.Y) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    out_.pack(side=tk.RIGHT,fill=tk.Y)
    scroll_1.config(command=out_.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    out_.config(yscrollcommand=scroll_1.set) # 将滚动条关联到文本框
    '''文本'''
    l=tk.Label(window,text='<--in | out-->',bg='white',width=15,height=2)
    l.pack()
    '''按钮'''
    btn0 = tk.Button(window,text = 'translation',width=15,height=2,command=traslating)
    btn0.pack()
    btn1 = tk.Button(window,text = 'clean',width=15,height=2,command=cleaning)
    btn1.pack()
    '''显示状态的标签'''
    foo="Show state"
    state=tk.Label(window,width=13,height=1,font=10,text=foo)
    state.pack(side=tk.BOTTOM)

    window.mainloop()#窗口不断刷新
