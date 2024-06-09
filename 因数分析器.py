import math as mt
import tkinter as tk
from tkinter import messagebox

def factor_analysis():
    try:
        n = int(entry.get())
        factors = factor(n)
        if len(factors) == 2:
            messagebox.showinfo("因数分析器", "该数为质数！")
        else:
            messagebox.showinfo("因数分析器", "因数为：" + str(factors))
    except ValueError:
        messagebox.showerror("因数分析器", "请输入整数！")
def factor(n):
    factors = []
    for i in range(1, int(mt.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n//i)
    return factors

root = tk.Tk()
root.title("因数分析器")
root.geometry("260x100")

label = tk.Label(root, text="请输入一个整数：")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="分析", command=factor_analysis, width=10)
button.pack()

root.mainloop()

