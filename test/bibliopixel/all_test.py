import os, unittest, BiblioPixelAnimations
from . import_all import import_all
from bibliopixel.util import log


class TestAll(unittest.TestCase):
    def _test(self, root, name, blacklist):
        _, failures = import_all(root, name, blacklist)
        for name, tb in failures:
            log.printer('*** Failed to load', name)
            log.printer()
            log.printer(tb)
            log.printer()

        self.assertTrue(not failures)

    def test_bp(self):
        self._test(BP_ROOT, BP_NAME, BP_BLACKLIST)

    def test_bpa(self):
        self._test(BPA_ROOT, BPA_NAME, BPA_BLACKLIST)


BP_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BP_NAME = 'bibliopixel'
BP_BLACKLIST = ['bibliopixel.drivers.PiWS281X']

BPA_ROOT = os.path.dirname(os.path.dirname(BiblioPixelAnimations.__file__))
BPA_NAME = 'BiblioPixelAnimations'
BPA_BLACKLIST = [
    'BiblioPixelAnimations.cube.spectrum',
    'BiblioPixelAnimations.cube.spectrum.system_eq',
    'BiblioPixelAnimations.matrix.ScreenGrab',
    'BiblioPixelAnimations.matrix.kimotion',
    'BiblioPixelAnimations.matrix.opencv_video',
    'BiblioPixelAnimations.matrix.spectrum',
    'BiblioPixelAnimations.matrix.spectrum.system_eq',
    'BiblioPixelAnimations.receivers.GenericNetworkReceiver',
]
