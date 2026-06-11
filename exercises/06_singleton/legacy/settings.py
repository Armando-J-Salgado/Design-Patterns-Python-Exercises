class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            instance.values = {}
            cls._instance = instance
        return cls._instance

    def set(self, key, value):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)


def settings():
    return AppSettings()
