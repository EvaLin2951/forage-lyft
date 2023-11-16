from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return self._current_date > service_threshold_date
