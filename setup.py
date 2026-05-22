from distutils.core import setup

setup(
    name='qt_widgets',
    author='Martin Privat',
    version='0.5.1',
    packages=['qt_widgets','qt_widgets.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='custom qt widgets and tools',
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={"qt_widgets": ["resources/*"]},
    install_requires=[
        "numpy",
        "qtpy",
    ],
    extras_require={
        "pyqt5": ["PyQt5"],
        "pyqt6": ["PyQt6"],
        "pyside6": ["PySide6"],
    }
)
