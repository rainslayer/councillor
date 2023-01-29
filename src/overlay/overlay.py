import tkinter as tk


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

    self.root.mainloop()

  def close_app(self, event):
    self.root.destroy()

  def start_rect(self, event):
    self.start_x, self.start_y = event.x, event.y
    self.rect = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg='black')
    self.rect.pack()

  def end_rect(self, event):
    end_x, end_y = event.x, event.y
    self.rect.create_rectangle(self.start_x, self.start_y, end_x, end_y, fill='white')

  def draw_rect(self, event):
    end_x, end_y = event.x, event.y
    self.rect.create_rectangle(self.start_x, self.start_y, end_x, end_y, fill='white', tags="rect")

