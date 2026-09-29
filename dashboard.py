import os, subprocess, sys, tkinter as tk
from tkinter import ttk
from pathlib import Path
from config import CSV_FILE
from database import init_database, get_today
class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title('Smart Face Attendance System'); self.geometry('900x600'); init_database()
        tk.Label(self,text='SMART FACE ATTENDANCE SYSTEM',font=('Segoe UI',20,'bold')).pack(pady=18)
        bar=tk.Frame(self); bar.pack(pady=5)
        ttk.Button(bar,text='Start Camera',command=lambda:subprocess.Popen([sys.executable,str(Path(__file__).with_name('main.py'))])).pack(side='left',padx=5)
        ttk.Button(bar,text='Refresh',command=self.refresh).pack(side='left',padx=5)
        ttk.Button(bar,text='Open CSV',command=lambda:os.startfile(str(CSV_FILE))).pack(side='left',padx=5)
        self.t=ttk.Treeview(self,columns=('name','id','date','time','status'),show='headings')
        for c,h in zip(self.t['columns'],['Name','ID','Date','Time','Status']): self.t.heading(c,text=h); self.t.column(c,width=150,anchor='center')
        self.t.pack(fill='both',expand=True,padx=20,pady=20); self.refresh()
    def refresh(self):
        for x in self.t.get_children(): self.t.delete(x)
        for row in get_today(): self.t.insert('', 'end', values=row)
if __name__=='__main__': App().mainloop()
