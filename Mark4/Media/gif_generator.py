#original code from:
#https://www.daniweb.com/programming/software-development/code/217060/show-animated-gif-files-python

from Evaluation import evaluation

import pyglet as pygl
import sys
import time

class Gif_Generator_Init:
    def __init__(self):
        super(Gif_Generator_Init, self).__init__()
        self.filename = []
        self.width = ''


class Gif_Generator(Gif_Generator_Init):

    def gif_animation(self):

        if evaluation.language_decision == 'idiot':
            self.filename = 'Gifs/idiot.gif'

        #pick an animated gif file you have in the working directory
        animation = pygl.resource.animation({self.filename})
        sprite = pygl.sprite.Sprite(animation)

        #create a window and set it to the image size
        win = pygl.window.Window(width=sprite.width, height=sprite.height)

        # set window background color = r, g, b, alpha
        # each value goes from 0.0 to 1.0
        green = 0, 1, 0, 1
        pygl.gl.glClearColor(*green)



        @win.event
        def on_draw():
            win.clear()
            sprite.draw()

        pygl.app.run()
        time.sleep(10)
        sys.exit()
