#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

root = tk.Tk()
root.title("Calculatrice")

display = tk.Entry(root, width=30)
display.pack(padx=10, pady=10)

root.mainloop()
