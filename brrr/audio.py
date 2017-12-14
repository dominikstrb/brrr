import os
import sys
from subprocess import call


def play(wavefile):
    """Cross-platform Sound Playing with StdLib only,No Sound file required."""

    if not os.path.isfile(wavefile) or not os.access(wavefile, os.R_OK):
        raise ValueError('"{}" is not a valid .wav file'.format(wavefile))

    if sys.platform.startswith("linux"):
        return call("chrt -i 0 aplay '{fyle}'".format(fyle=wavefile), shell=1)
    if sys.platform.startswith("darwin"):
        return call("afplay '{fyle}'".format(fyle=wavefile), shell=True)
    if sys.platform.startswith("win"):  # FIXME: This is Ugly.
        return call("start /low /min '{fyle}'".format(fyle=wavefile), shell=1)
