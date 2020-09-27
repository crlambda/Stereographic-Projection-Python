def draw(vector, indice):
    ax.scatter(vector[:,0], vector[:,1], vector[:,2], s=50, alpha=0.35)
    for i in range (len(vector)):
        x, y, z = vector[i]
        if np.abs(indice[i][0]) < 2 and np.abs(indice[i][1]) < 2 and np.abs(indice[i][2]) < 2:
            ax.text(x, y, z, f'{indice[i][0]:>2d} {indice[i][1]:>2d} {indice[i][2]:>2d}') 

from lotsofdots import Lots_Of_Dots
import tkinter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from projection import Projection

root = tkinter.Tk()
root.wm_title("Stereographic Projection")
fig = Figure(figsize=(7, 7), dpi=100)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=0,azim=0)
draw(Lots_Of_Dots([1,-1,0]).dsphere, Lots_Of_Dots([1,-1,0]).dots)
draw(Lots_Of_Dots([1,1,0]).dsphere, Lots_Of_Dots([1,1,0]).dots)
draw(Lots_Of_Dots([1,0,1]).dsphere, Lots_Of_Dots([1,0,-1]).dots)
draw(Lots_Of_Dots([1,0,-1]).dsphere, Lots_Of_Dots([1,0,-1]).dots)
draw(Lots_Of_Dots([0,-1,1]).dsphere, Lots_Of_Dots([0,-1,1]).dots)
draw(Lots_Of_Dots([0,1,1]).dsphere, Lots_Of_Dots([0,1,1]).dots)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()