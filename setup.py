from distutils.core import setup, find_packages

setup(
    name='qt_widgets',
    author='Martin Privat',
    version='0.3.17',
    packages=['qt_widgets','qt_widgets.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='custom qt widgets and tools',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "PyQt5",
    ]
)
