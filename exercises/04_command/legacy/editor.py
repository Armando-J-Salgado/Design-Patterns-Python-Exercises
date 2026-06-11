class Editor:
    def __init__(self):
        self.text = ""
        self.history = []

    def execute(self, action, value=None):
        if action == "insert":
            self.history.append(self.text)
            self.text = f"{self.text}{value}"
            return self.text

        if action == "delete":
            self.history.append(self.text)
            count = int(value or 0)
            self.text = self.text[:-count] if count else self.text
            return self.text

        if action == "replace":
            self.history.append(self.text)
            old, new = value
            self.text = self.text.replace(old, new, 1)
            return self.text

        if action == "undo":
            if self.history:
                self.text = self.history.pop()
            return self.text

        return self.text
