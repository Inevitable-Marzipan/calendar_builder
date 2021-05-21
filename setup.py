from setuptools import setup

setup(
    name="calendar_builder",
    version="0.1.0",
    packages=["calendar_builder"],
    install_requires = ["dominate"],
    entry_points={
        "console_scripts": [
            "calendar_builder = calendar_builder.__main__:main"
        ]
    },
)