"""
Write a Python script that prints out information of the version of Python
running using the sys module.
"""

import sys

if __name__ == "__main__":
    version_info = sys.version.split()
    print(version_info)
    print(f"Python version {version_info[0]}")
    print(f"Build date: {' '.join(version_info[1:6])}")
    print(f"License Info: {' '.join(version_info[6:8])}")