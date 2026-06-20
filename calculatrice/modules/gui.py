#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def main() -> None:
    root = tk.Tk()
    root.title("Calculatrice")

    display = tk.Entry(root, width=30)
    display.pack(padx=10, pady=10)

    def insert_character(c: str) -> None:
        display.insert(tk.END, c)
    for digit in range(10):
        button = tk.Button(
            root,
            text=str(digit),
        command= lambda d=digit: insert_character(str(d))
        )
        button.pack()

    root.mainloop()

