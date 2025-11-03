from distutils.core import setup

setup(
    name='qt_widgets',
    author='Martin Privat',
    version='0.4.10',
    packages=['qt_widgets','qt_widgets.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='custom qt widgets and tools',
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={"qt_widgets": ["resources/*"]},
    install_requires=[
        "numpy",
        "PyQt5",
    ]
)
