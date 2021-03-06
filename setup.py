try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fnordload',
    version='1.0.0',
    description='fnordload',
    author='',
    author_email='',
    url='https://github.com/muccc/fnordload',
    packages=['fnordload'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='upay',
    license='GPLv3+',
    install_requires=['upay', 'max7301', 'lcdproc', 'pyserial', 'eSSP'],
    scripts=['scripts/fnordload']
)
