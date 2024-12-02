import time
from re import match

import keyboard
import mouse
from PyQt6.QtWidgets import QFormLayout

import Consts


class Sleep:
    def __init__(self, time=0):
        self.time = time

    def play(self):
        time.sleep(self.time)


class MouseAction:
    NOTHING = 0
    SINGLE_CLICK = 1
    DOUBLE_CLICK = 2
    PRESS = 3
    RELEASE = 4

    LMB = 5
    RBM = 6
    CBM = 7

    DRAG = 8
    MOVE = 9

    def __init__(self, action=None, button=None, action_move=None,
                 x_y=tuple(), duration=0, wheel=0):
        self.action = action
        self.button = button
        self.action_move = action_move
        self.x_y = x_y
        self.duration = duration
        self.wheel = wheel
        self.arr = [action, button, action_move, x_y[0], x_y[1], duration, wheel]

    def play(self):
        if self.SINGLE_CLICK == self.action:
            mouse.click(button=self.button)
        elif self.DOUBLE_CLICK == self.action:
            mouse.double_click(button=self.button)
        elif self.PRESS == self.action:
            mouse.press(button=self.button)
        elif self.RELEASE == self.action:
            mouse.release(button=self.button)

        if self.DRAG == self.action_move:
            mouse.move(*self.x_y, duration=self.duration, absolute=False)
        elif self.DRAG == self.action_move:
            mouse.move(*self.x_y, duration=self.duration)

        mouse.wheel(self.wheel)


class KeyboardAction:
    def __init__(self, key=None, press=None, release=None, send=None, write=None, delay=0, text=None):
        self.key = key
        self.press = press
        self.release = release
        self.send = send
        self.write = write
        self.delay = delay
        self.text = text

    def play(self):
        if self.press:
            keyboard.press(self.key)
        elif self.release:
            keyboard.release(self.key)
        elif self.send:
            keyboard.send(self.key)
        elif self.write:
            keyboard.write(self.text, delay=self.delay)
