class Bind:
    def __init__(self, name, hotkey, actions):
        self.name = name
        self.hotkey = hotkey
        self.actions = actions

    def play(self):
        for action in self.actions:
            action.play()


