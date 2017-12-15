from setuptools import setup
setup(
  name = 'brrr',
  packages = ['brrr'], # this must be the same as the name above
  version = '0.12',
  description = 'Let Gucci Mane tell you when your script is done.',
  author = 'Dominik Straub',
  author_email = 'dstraub93@gmail.com',
  url = 'https://github.com/dominikstrb/brrr', # use the URL to the github repo
  download_url = 'https://github.com/dominikstrb/brrr/archive/master.zip', # I'll explain this in a second
  keywords = ['gucci', 'skrrrahh', 'brrr'], # arbitrary keywords
  classifiers = [],
  python_requires='>=3',
  package_data={'brrr': ['adlibs/*.wav']},
)
