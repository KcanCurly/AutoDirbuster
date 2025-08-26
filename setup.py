from setuptools import setup, find_packages

setup(
    name="AutoDirbuster",
    version="1.0.0",
    author="KcanCurly",
    description="Automatically run and save ffuf scans for multiple IPs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/AutoDirbuster",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dnspython"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "AutoDirbuster=src.AutoDirbuster:main",  
        ],
    },
)