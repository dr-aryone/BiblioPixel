from . base import BaseAnimation


class OffAnim(BaseAnimation):
    """A trivial animation that turns all LEDs off."""

    def __init__(self, led, timeout=10):
        super().__init__(led)
        self.internal_delay = timeout

    def step(self, amt=1):
        self._led.all_off()
