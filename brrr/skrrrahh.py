import os
import warnings
import random

from .audio import play

sounds = {"twochainz": "twochainz.wav",
          "twochainz1": "twochainz1.wav",
          "bigboi": "bigboi.wav",
          "biggie": "biggie.wav",
          "bigsean": "bigsean.wav",
          "bigsean1": "bigsean1.wav",
          "bigsean2": "bigsean2.wav",
          "bigsean3": "bigsean3.wav",
          "bigsean4": "bigsean4.wav",
          "bigsean5": "bigsean5.wav",
          "bigshaq": "bigshaq.wav",
          "birdman": "birdman.wav",
          "birdman1": "birdman1.wav",
          "birdman2": "birdman2.wav",
          "busta": "busta.wav",
          "chance": "chance.wav",
          "desiigner": "desiigner.wav",
          "diddy": "diddy.wav",
          "drake": "drake.wav",
          "drake1": "drake1.wav",
          "drummaboy": "drummaboy.wav",
          "fetty": "fetty.wav",
          "flava": "flava.wav",
          "future": "future.wav",
          "gucci": "gucci.wav",
          "gucci1": "gucci1.wav",
          "gucci2": "gucci2.wav",
          "jayz": "jayz.wav",
          "jayz1": "jayz1.wav.wav",
          "kendrick": "kendrick.wav",
          "khaled": "khaled.wav",
          "khaled1": "khaled1.wav",
          "khaled2": "khaled2.wav",
          "khaled3": "khaled3.wav",
          "liljon": "liljon.wav",
          "liljon1": "liljon1.wav",
          "nicki": "nicki.wav",
          "pitbull": "pitbull.wav",
          "ross": "ross.wav",
          "ross1": "ross1.wav",
          "schoolboy": "schoolboy.wav",
          "snoop": "snoop.wav",
          "soulja": "soulja.wav",
          "takeoff": "takeoff.wav",
          "tpain": "tpain.wav",
          "traviscott": "traviscott.wav",
          "treysongz": "treysongz.wav",
          "trick": "trick.wav",
          "waka": "waka.wav",
          "weezy": "weezy.wav",
          "yg": "yg.wav"}

PATH = 'adlibs/'


def skrrrahh(sound=None):

    if sound not in sounds.keys():
        if isinstance(sound, int) and sound < len(sounds):
            sound_path = os.path.join(os.path.dirname(__file__), PATH, list(sounds.values())[sound])
        elif isinstance(sound, str) and os.path.isfile(sound) and os.access(sound, os.R_OK):
            sound_path = sound
        else:
            if sound is not None:
                warnings.warn(
                    'Sound must be either a valid sound indicator (see README), a number between 0 and {}, or a valid path to a sound file'.format(
                        len(sounds) - 1))
            sound = random.randint(0, len(sounds) - 1)
            sound_path = os.path.join(os.path.dirname(__file__), PATH, list(sounds.values())[sound])
    else:
        sound_path = os.path.join(os.path.dirname(__file__), PATH, sounds[sound])

    play(sound_path)
