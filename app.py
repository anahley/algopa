"""
This is the GUI for Algopa.
"""
import tkinter as tk
from tkinter import filedialog, Text
import os


def buy():
    print("Hello")

def init():
    root = tk.Tk()  # root is the base
    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()
    button_buy = tk.Button(root, text="Buy one share of AAPL", padx=10, pady=5, fg="white", bg="#436A73", command=buy)
    button_buy.pack()
    return root


def main():
    init().mainloop()


if __name__ == "__main__":
    main()
