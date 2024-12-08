import time

import keyboard
import mouse
from PyQt6.QtCore import QSettings

import Consts


class Cycle:
    def __init__(self, always, n, arr):
        self.always = always
        self.n = n
        self.arr = arr

    def play(self, hotkey):
        settings = QSettings()
        if self.always:
            while True:
                stops = settings.value(Consts.SETTINGS_STOPS, set())
                if hotkey in stops:
                    return None
                for action in self.arr:
                    action.play(hotkey)
        else:
            for _ in range(self.n):
                stops = settings.value(Consts.SETTINGS_STOPS, set())
                if hotkey in stops:
                    return None
                for action in self.arr:
                    action.play(hotkey)


class Sleep:
    def __init__(self, time=0):
        self.time = time / 1000

    def play(self, hotkey):
        settings = QSettings()
        stops = settings.value(Consts.SETTINGS_STOPS, set())
        if hotkey in stops:
            return None
        time.sleep(self.time)



class MouseAction:
    NOTHING = Consts.NOTHING
    SINGLE_CLICK = Consts.SINGLE_CLICK
    DOUBLE_CLICK = Consts.DOUBLE_CLICK
    PRESS = Consts.PRESS
    RELEASE = Consts.RELEASE

    LMB = Consts.LMB
    RBM = Consts.RMB
    CBM = Consts.MOUSE_WHEEL

    DRAG = Consts.ON
    MOVE = Consts.IN

    def __init__(self, action=None, button=None, action_move=None,
                 x_y=tuple(), duration=0, wheel=0):
        self.action = action
        self.button = button
        self.action_move = action_move
        self.x_y = x_y
        self.duration = duration
        self.wheel = wheel
        self.arr = [action, button, action_move, x_y[0], x_y[1], duration, wheel]

    def play(self, hotkey):
        settings = QSettings()
        stops = settings.value(Consts.SETTINGS_STOPS, set())
        if hotkey in stops:
            return None
        if self.DRAG == self.action_move:
            mouse.move(*self.x_y, duration=self.duration, absolute=False)
        elif self.MOVE == self.action_move:
            mouse.move(*self.x_y, duration=self.duration)

        if self.SINGLE_CLICK == self.action:
            mouse.click(button=self.button)
        elif self.DOUBLE_CLICK == self.action:
            mouse.double_click(button=self.button)
        elif self.PRESS == self.action:
            mouse.press(button=self.button)
        elif self.RELEASE == self.action:
            mouse.release(button=self.button)

        mouse.wheel(self.wheel)


class KeyboardAction:
    SINGLE_CLICK = Consts.SINGLE_CLICK
    PRESS = Consts.PRESS
    RELEASE = Consts.RELEASE
    WRITE_TEXT = Consts.WRITE_TEXT

    def __init__(self, key=None, action=None ,text=None):
        self.key = key
        self.action = action
        self.text = text

    def play(self, hotkey):
        settings = QSettings()
        stops = settings.value(Consts.SETTINGS_STOPS, set())
        if hotkey in stops:
            return None
        if self.action == self.PRESS:
            keyboard.press(self.key)
        elif self.action == self.RELEASE:
            keyboard.release(self.key)
        elif self.SINGLE_CLICK == self.action:
            keyboard.send(self.key)
        elif self.WRITE_TEXT == self.action:
            keyboard.write(self.text)
