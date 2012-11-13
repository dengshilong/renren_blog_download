from download import *
from login import *

    
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root = tkinter.Tk()
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label_user = Label(frame, text="用户名")
        self.label_user.pack(side=LEFT)
        self.entry_user = Entry(frame)
        self.entry_user.pack(side=LEFT)
        self.label_password = Label(frame, text="密码")
        self.label_password.pack(side=LEFT)
        self.entry_password = Entry(frame)
        self.entry_password.pack(side=LEFT)
        self.button_download = Button(frame, text="下载", command=self.download)
        self.button_download.pack()

    def download(self):
        user = self.entry_user.get()
        password = self.entry_password.get()
        rr = Renren()
        home = rr.login(user,password)
        if not home:
            messagebox.showinfo("错误","用户名或密码错误，请重新输入")
            return False
        else:
            fd = filedialog.asksaveasfile()
            path = fd.name
            messagebox.showinfo("下载中","下载文章中，请耐心等待，点击确定继续下载")
            get_blog(home,path)
            messagebox.showinfo("下载完成","下载完成，关闭程序，查看下载结果")
            return True
        

if __name__ == '__main__':
    root = Tk(className="人人网日志下载工具")
    app = App(root)
    root.mainloop()
    
   
    



