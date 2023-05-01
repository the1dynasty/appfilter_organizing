#!/usr/bin/env python

import os

# Get the directory path of the script file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Specify the folder path where the PNG files and the appfilter.xml file are located
FOLDER_PATH = SCRIPT_DIR

# Get the list of PNG files in the folder
#PNG_FILES = [os.path.join(FOLDER_PATH, f) for f in os.listdir(FOLDER_PATH) if f.endswith(".png")]

# Get the list of PNG and WebP files in the folder
PNG_FILES = [os.path.join(FOLDER_PATH, f) for f in os.listdir(FOLDER_PATH) if f.endswith(".png")]
WEBP_FILES = [os.path.join(FOLDER_PATH, f) for f in os.listdir(FOLDER_PATH) if f.endswith(".webp")]
IMAGE_FILES = PNG_FILES + WEBP_FILES

# Create a new file for storing the modified appfilter.xml
MODIFIED_FILE = os.path.join(FOLDER_PATH, "appfilter_modified.xml")

# Read the appfilter.xml file line by line and write matching lines to the output file
with open(os.path.join(FOLDER_PATH, "appfilter.xml"), "r") as input_file, open(MODIFIED_FILE, "w") as output_file:
    drawables = []
    for line in input_file:
        # Check if the line contains a drawable attribute
        if 'drawable="' in line:
            # Extract the drawable name from the line
            drawable_name = line.split('drawable="')[1].split('"')[0]
            # Check if the drawable name is in the list of PNG files
            #if os.path.join(FOLDER_PATH, drawable_name + '.png') in PNG_FILES:
            if os.path.join(FOLDER_PATH, drawable_name + '.png') in IMAGE_FILES or os.path.join(FOLDER_PATH, drawable_name + '.webp') in IMAGE_FILES:
                # If there is a matching drawable name, add the line to the list of drawable lines
                drawables.append(line)
                continue
        # Write the line to the new file
        output_file.write(line)

# Sort the list of drawable lines based on the drawable attribute
drawables.sort(key=lambda x: x.split('drawable="')[1].split('"')[0])

# Create the output file with the sorted items and copy over the other lines
with open(os.path.join(FOLDER_PATH, "appfilter_organized.xml"), "w") as output_file:
    output_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    for line in open(os.path.join(FOLDER_PATH, "appfilter.xml")):
        if 'drawable="' not in line:
            if '</resources>' not in line and '<?xml' not in line:
                output_file.write(line)
    for drawable in drawables:
        output_file.write('    ' + drawable.strip() + '\n')
    output_file.write('</resources>\n')
