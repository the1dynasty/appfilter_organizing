# README - How to Use "Appfilter Organizer"

## Introduction
This README file provides instructions on how to use the "gui.py" script in conjunction with the "appfilter_script.py" script. Both of these scripts must be located in the same folder in order to function correctly.

## Requirements
In order to run the scripts, you will need the following:
- Python 3.x installed on your computer
- The "gui.py" and "appfilter_script.py" scripts located in the same folder
- Tkinter: This is used to create the GUI.
- ttkthemes: This is used to set the Material Design style for the GUI.
- The PNG images for your theme AND the appfilter.xml file in a folder together. (Does not have to be the same folder as the "gui.py" and "appfilter_script.py")

## OPTION 1: Running the Script with the GUI
To run the "gui.py" script, follow these steps:

1. Download the "Appfilter_Organized.zip" file and extract it wherever it's convenient.
2. Open a command prompt or terminal window.
3. Navigate to the folder where the scripts are located using the "cd" command.
4. Type the following command to run the script:

``` python3 gui.py ```

4. Press Enter to execute the command.
5. The GUI will now be launched and you can use it to interact with the "appfilter_script.py" script.

## Using the GUI
The GUI allows you to select the folder where your appfilter.xml file and PNG images are located.

Once you have selected the folder, you can click the "Organize" button to execute the "appfilter_organizer.py" script. The script will then read in the appfilter.xml file, organize the apps based on the drawable name in ascending alphabetical order, and save the new file as appfilter_organized.xml to the same folder as your PNG and appfilter.xml. This will NOT overwrite your original "appfilter.xml".

## Conclusion
With these instructions, you should now be able to use the "gui.py" script to organize your appfilter.xml file by drawable name in ascending alphabetical order.


## OPTION 2: Running the script without using the GUI

If you are skipping the GUI and want to run the script directly follow these steps:
- Place the "appfilter_script.py" in the same folder as your PNG images AND your appfilter.xml.
1. Dowload just the "appfilter_script.py" file.
2. Place the "appfilter_script.py" in the same folder as your PNG images AND your appfilter.xml.
3. Open a command prompt or terminal window.
4. Navigate to the folder where the scripts are located using the "cd" command.
5. Type the following command to run the script:

``` python3 appfilter_script.py ```

## Note

- If your system uses another version of Python simply use "python" instead of "python3" to execute the commands.
- This script is only compatible with appfilter.xml files for Android launchers.
- If you want to run this script on Windows, you may need to modify the script to use "python" instead of "python3" in the command.

## Support
If you encounter any issues while using the Appfilter Organizer tool, please feel free to open an issue on our GitHub repository. We will do our best to assist you as quickly as possible.
