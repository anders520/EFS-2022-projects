'''show_state_array.py
This Python module provides the means to use Tk graphics to display a
state visualization that consists of a 2D array of colored boxes, and
possibly some textual labels on them.

It is meant to be used together with the Tk_SOLUZION_Client.py program,
and an appropriately structured problem formulation file and visualization
file such as Missionaries.py and Missionaries_Array_VIS_FOR_TK.py



Version of Aug. 29, 2018. Prints fewer diagnostics than the version of
 Aug. 6, 2017.
S. Tanimoto

'''
import tkinter as tk

STATE_WINDOW = None


class state_array:

  def __init__(self, color_array=[], string_array=None, column_headers=[],
               column_footers=[],row_labels_left=[],row_labels_right=[],
               text_color="white",
               text_font=None,
               background=(128,128,128),
               caption="Current State"):
    self.color_array=color_array
    self.string_array=string_array
    self.column_headers=column_headers
    self.column_footers=column_footers
    self.row_labels_left=row_labels_left
    self.row_labels_right=row_labels_right
    self.text_color=text_color
    self.text_font=text_font
    self.background=background
    self.caption=caption
    self.ncols = len(self.color_array[0])
    self.nrows = len(self.color_array)

  def show(self):
    global STATE_WINDOW
    x0 = 0; y0 = 0;
    cellw = STATE_WINDOW.width / self.ncols
    cellh = STATE_WINDOW.height / self.nrows
    i = 0
    for r in self.color_array:
      j = 0
      for c in r:
        #print(c, end=' ')
        tk_rgb = "#%02x%02x%02x" % c
        STATE_WINDOW.canvas.create_rectangle(x0+j*cellw, y0+i*cellh,
                                             x0+(j+1)*cellw, y0+(i+1)*cellh,
                                             fill=tk_rgb)
        if self.string_array:
          STATE_WINDOW.canvas.create_text(x0+(j+0.5)*cellw, y0+(i+0.5)*cellh,
                                          text=self.string_array[i][j],
                                          fill=self.text_color,
                                          font=self.text_font)
        j += 1
      i += 1
      print()
    STATE_WINDOW.label.config(text=self.caption)


class state_display(tk.Frame):
  def __init__(self, parent, width=300, height=300):
    super(state_display, self).__init__(parent)
    self.width=width; self.height=height
    self.canvas = tk.Canvas(parent, width=self.width, height=self.height)
    self.canvas.pack()
    self.label = tk.Label(self, text="caption goes here")
    self.label.pack(padx=20, pady=20)
      

def initialize_tk(width=300, height=300, title='State Display Window'):
  global STATE_WINDOW
  root = tk.Tk()
  root.title(title)
  the_display = state_display(root, width=width, height=height)
  the_display.pack(fill="both", expand=True)
  STATE_WINDOW = the_display
  print("VIS initialization finished")

def test():
  initialize_tk()
  two_by_two = state_array(color_array=[[(255,0,0),(0,255,0)],[(0,0,255),(255,0,0)]],
                           string_array=[["R","G"],["B","R"]],
                           background=(92,0,128))
  two_by_two.show()
#test()
if __name__=="__main__":
  test()
  

