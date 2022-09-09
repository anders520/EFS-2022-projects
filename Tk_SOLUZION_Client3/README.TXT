README.TXT

This folder contains a version of the Tk_SOLUZION_Client that makes it easy to
include images in state visualizations.

This client creates a GUI so that the user can play a game or solve a problem
by selecting operators from a combo box in the GUI, and clicking a button.
So no typing is necessary.

The graphical format is based on the old show_state_array approach, but
that file is not needed, since its capabilities have been integrated into
the main client Python file Tk_SOLUZION_Client.

If you were using the old show_state_array approach to creating your
visualization, you should probably switch to this new client, even if
you don't need to use images.  It does have a memory leak fixed that was
not fixed in show_state_array.  You should not have to make any changes
except to edit file names or extensions in a couple of places.

If you are not using images, you can comment out the couple of lines
of code where the program is trying to import submodules from PIL.

If you do want to use images, you will need Pillow installed for your
system and Python environment.  Doing that was explained in an ED post and
discussed in class.   Once that is working you can put .jpg files in your
game folder and in the visualization, put their filenames in the array
locations where you want the images to show up (instead of a colored
colored rectangle).  The image will be automatically resized to fit into
the grid.  If you try running the Missionaries example, you'll see what
happens.  Then look at the code in Missionaries3_VIS_FOR_TK3.py to see
how to set up this kind of visualization.

S. Tanimoto, 17 September 2019.

