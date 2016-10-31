#!/usr/bin/python3
import os
import easygui

def main():
	plugin_file_name = easygui.enterbox("Enter the folder name for your plugin. Ex: 'my-plugin' ")

	for dname, dirs, files in os.walk(os.path.join(os.getcwd(), "plugin-name")):

		for fname in files:
			fpath = os.path.join(dname, fname)
			#First change file CONTENTS
			with open(fpath) as f:
				s = f.read()
				s = s.replace("plugin-name", plugin_file_name)
				with open(fpath, "w") as f:
					f.write(s)

	easygui.msgbox("All done, get codin'!")


if __name__ == '__main__':
	main()