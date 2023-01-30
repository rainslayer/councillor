import sys
import tkinter as tk

from PIL import ImageGrab


class Overlay:
  def __init__(self):
    self.rect = None
    self.start_y = None
    self.start_x = None

    self.root = tk.Tk()
    self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
    self.root.config(bg="black")
    self.root.attributes("-alpha", 0.5)
    self.root.attributes("-fullscreen", True)

    self.root.bind("<Escape>", self.close_app)
    self.root.bind("<Button-1>", self.start_rect)
    self.root.bind("<ButtonRelease-1>", self.end_rect)
    self.root.bind("<B1-Motion>", self.draw_rect)

    self.rect = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(),
                          bg='black')

    self.root.mainloop()

  def close_app(self, event):
    self.root.destroy()

  def start_rect(self, event):
    self.start_x, self.start_y = event.x, event.y
    self.rect.pack()

  def end_rect(self, event):
    end_x, end_y = event.x, event.y

    if end_x < self.start_x:
      x = end_x
      x1 = self.start_x
    else:
      x = self.start_x
      x1 = end_x

    if end_y < self.start_y:
      y = end_y
      y1 = self.start_y
    else:
      y = self.start_y
      y1 = end_y

    self.root.destroy()
    ImageGrab.grab(bbox=(x, y, x1, y1)).save("screenshot.png")
    sys.exit()

  def draw_rect(self, event):
    end_x, end_y = event.x, event.y
    self.rect.delete("rect")
    self.rect.create_rectangle(self.start_x, self.start_y, end_x, end_y, fill='white', tags="rect")
