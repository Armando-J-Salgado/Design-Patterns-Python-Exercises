from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from weather import WeatherStation


class Recorder:
    def __init__(self):
        self.values = []

    def update(self, reading):
        self.values.append(reading)


def test_listeners_receive_updates():
    station = WeatherStation()
    callback_values = []
    recorder = Recorder()

    station.add_listener(lambda reading: callback_values.append(reading))
    station.add_listener(recorder)
    station.set_reading(21, 55)

    assert callback_values == [{"temperature": 21, "humidity": 55}]
    assert recorder.values == [{"temperature": 21, "humidity": 55}]


def test_listener_can_be_removed():
    station = WeatherStation()
    callback_values = []

    def listener(reading):
        callback_values.append(reading)

    station.add_listener(listener)
    station.remove_listener(listener)
    station.set_reading(18, 60)

    assert callback_values == []
