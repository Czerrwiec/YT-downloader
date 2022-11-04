from distutils.core import setup
import py2exe

setup(
    windows=[{
        'script': 'YT downloader.py',
        "icon_resources": [(1, "ytico.ico")]
    }]
)
