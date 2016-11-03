# Automated WordPress Plugin Boilerplate

## Contents

The WordPress Plugin Boilerplate includes the following files:

* .gitignore. Used to exclude certain files from the repository.
* CHANGELOG.md. The list of changes to the core project.
* README.md. The file that you’re currently reading.
* A plugin-name directory that contains the source code - a fully executable WordPress plugin.
* setup.py. Script that automates creation and renaming of your plugin using a GUI.

## Requirements

* [easygui](http://easygui.readthedocs.io/en/latest/#how-to-get-easygui)
* Python

## Installation

* Install easygui if you don't already have it.
`pip install easygui`
* Clone or download this repo.
* `cd` into the directory and run `python setup.py`
* Follow the GUI instructions

## Important Notes
As the GUI states, your plugin name should be all lowercase and seperated by hyphens. For example, `my-new-plugin`

## Credits
Originally forked from [WordPress-Plugin-Boilerplate](https://github.com/DevinVinson/WordPress-Plugin-Boilerplate)