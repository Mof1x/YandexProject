from threading import Thread

import keyboard
from PyQt6.QtCore import QSettings, QRunnable, pyqtSlot, QThreadPool
from PyQt6.QtGui import QShortcut, QKeySequence

import Consts


class Bind:
    def __init__(self, name, hotkey, actions):
        self.name = name
        self.hotkey = hotkey
        self.actions = actions


class BindThread(QRunnable):
    def __init__(self, bind):
        self.name = bind.name
        self.hotkey = bind.hotkey
        self.actions = bind.actions
        self.flag = False
        self.settings = QSettings()
        super().__init__()

    @pyqtSlot()
    def run(self):
        self.threadpool = QThreadPool()
        plays = self.settings.value(Consts.SETTINGS_PLAYS)
        stops = self.settings.value(Consts.SETTINGS_STOPS)
        if self.hotkey not in plays:
            keyboard.add_hotkey(self.hotkey, self.flagUp)
            plays.append(self.hotkey)
            self.settings.setValue(Consts.SETTINGS_PLAYS, plays)
            for action in self.actions:
                action.play(self.name)
            if self.hotkey in plays:
                plays.remove(self.hotkey)
            if self.hotkey in stops:
                stops.remove(self.hotkey)
            try:
                keyboard.remove_hotkey(self.hotkey)
            except Exception:
                pass
            self.settings.setValue(Consts.SETTINGS_PLAYS, plays)
            self.settings.setValue(Consts.SETTINGS_STOPS, stops)

    def flagUp(self):
        stops = self.settings.value(Consts.SETTINGS_STOPS)
        try:
            stops.append(self.hotkey)
            self.settings.setValue(Consts.SETTINGS_STOPS, stops)
        except Exception:
            pass
