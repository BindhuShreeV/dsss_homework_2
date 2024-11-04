from setuptools import setup, find_packages

setup(
    name="math_quiz_package",
    version="1.0",
    packages=find_packages(),               # Automatically find packages in the directory
    install_requires=open("requirements.txt").read().splitlines(),  # Include requirements
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz_package.math_quiz:math_quiz",  # Adjusted for new package path
        ],
    },
    author="ma41rode",
    description="A simple math quiz application",
)
