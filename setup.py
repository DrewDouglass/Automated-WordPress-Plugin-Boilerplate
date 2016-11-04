#!/usr/bin/python3
import os
import easygui

def main():
	plugin_file_name = easygui.enterbox("Enter the folder name for your plugin. Ex: 'my-plugin' Keep it lowercase and use dashes (-)!")
	plugin_name_underscore = plugin_file_name.replace("-", "_")
	plugin_class_name = plugin_name_underscore.title()

	for dname, dirs, files in os.walk(os.path.join(os.getcwd(), "plugin-name")):

		for fname in files:
			fpath = os.path.join(dname, fname)
			#First change file CONTENTS
			with open(fpath) as f:
				s = f.read()
				s = s.replace("plugin-name", plugin_file_name)
				with open(fpath, "w") as f:
					f.write(s)
			#underscores
			with open(fpath) as f:
				s = f.read()
				s = s.replace("plugin_name", plugin_name_underscore)
				with open(fpath, "w") as f:
					f.write(s)
			#Plugin_Name (classes)
			with open(fpath) as f:
				s = f.read()
				s = s.replace("Plugin_Name", plugin_class_name)
				with open(fpath, "w") as f:
					f.write(s)
			if "plugin-name" in fname:
				#print(dname + fname)
				new_file_name = fname.replace("plugin-name", plugin_file_name)
				os.rename(os.path.join(dname, fname), os.path.join(dname, new_file_name))
	#Finally, rename the main plugin folder
	os.rename(os.path.join(os.getcwd(), "plugin-name"), os.path.join(os.getcwd(), plugin_file_name))

	easygui.msgbox("All done, get codin'!")


if __name__ == '__main__':
	main()