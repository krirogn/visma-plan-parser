# visma-plan-parser
The visma-plan-parser is a program that converts a .html from Visma InSchool into another more readable format.

## Usage
To use the program you use the syntax "visma-plan-parser FORMAT FILE DESTINATION". And example would be "visma-plan-parser json p.html p.json"

## Formats
The supported formats are currently:
- JSON 3D array object
- Web, as a basic .html file (mostly for debugging; DO NOT USE)

## Installing
To install the visma-plan-parser you have to download the bin from the releases tab, and then you can run it like any other executable.

## Compiling
To compile from source you have to git clone the repo, and then run "pyinstaller --onefile visma-plan-parser.py". You need to have "python3.7", "pip", "pyinstaller" and "BeautifulSoup4" installed.
