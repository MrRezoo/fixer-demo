from setuptools import setup

setup(
    name="fixer-demo",
    version="0.3",
    description="Fixer service demo packages",
    url="https://github.com/MrRezoo/fixer-demo.git",  # Git repository
    author="Reza Mobaraki",
    author_email="rezam578@gmail.com",
    license="MIT",
    pakages=['fixer'],
    install_requires=['requests'],
    zip_safe=False
)
