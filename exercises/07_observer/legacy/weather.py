class WeatherStation:
    def __init__(self):
        self.reading = None
        self.listeners = []

    def add_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def set_reading(self, temperature, humidity):
        self.reading = {"temperature": temperature, "humidity": humidity}
        for listener in list(self.listeners):
            if hasattr(listener, "update"):
                listener.update(self.reading)
            else:
                listener(self.reading)
