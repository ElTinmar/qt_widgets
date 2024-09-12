from distutils.core import setup

setup(
    name='qt_widgets',
    author='Martin Privat',
    version='0.3.5',
    packages=['qt_widgets','qt_widgets.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='custom qt widgets and tools',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy",
        "PyQt5",
    ]
)
