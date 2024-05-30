class Duration:
    def __init__(self, duration_in_sec):
        self.duration_in_sec = duration_in_sec

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)

    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)

    @property
    def seconds(self):
        return self.duration_in_sec

    @property
    def minutes(self):
        return self.duration_in_sec / 60

    @property
    def hours(self):
        return self.duration_in_sec / 3600
