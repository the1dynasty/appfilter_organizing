#!/bin/bash

# Get the directory path of the script file
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Specify the folder path where the PNG files and the appfilter.xml file are located
FOLDER_PATH="$SCRIPT_DIR"

# Get the list of PNG files in the folder
PNG_FILES=("$FOLDER_PATH"/*.png)

# Create a new file for storing the modified appfilter.xml
MODIFIED_FILE="$FOLDER_PATH/appfilter_modified.xml"

# Read the appfilter.xml file line by line and write matching lines to the output file
while read -r line; do
    # Check if the line contains a drawable attribute
    if [[ $line == *"drawable=\""* ]]; then
        # Extract the drawable name from the line
        DRAWABLE_NAME=$(echo "$line" | grep -o 'drawable="[a-zA-Z0-9_]*"' | cut -d '"' -f 2)
        # Check if the drawable name is in the list of PNG files
        if [[ " ${PNG_FILES[*]} " =~ " ${FOLDER_PATH}/${DRAWABLE_NAME}.png " ]]; then
            # If there is a matching drawable name, write the line to the new file
            echo "$line" >> "$MODIFIED_FILE"
        fi
    else
        # If the line does not contain a drawable attribute, write it to the new file
        echo "$line" >> "$MODIFIED_FILE"
    fi
done < "$FOLDER_PATH/appfilter.xml"

#!/bin/bash

# Extract the lines containing "drawable" from the input file and sort them based on the "drawable" attribute
drawables=$(grep 'drawable=' appfilter_modified.xml | sed -r 's/(.*)(drawable="[a-zA-Z0-9_]*")(.*)/\2 \1&\3/' | sort)

# Create the output file with the sorted items and copy over the other lines
cat > appfilter_organized.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<resources>
EOF

while read -r line; do
  if [[ "$line" =~ drawable= ]]; then
    component=$(echo "$line" | sed -n 's/.*component="\([^"]*\)".*/\1/p')
    drawable=$(echo "$line" | sed -n 's/.*drawable="\([^"]*\)".*/\1/p')
    echo "<item component=\"$component\" drawable=\"$drawable\" />" >> appfilter_organized.xml
  else
    echo "$line" >> appfilter_organized.xml
  fi
done < <(grep -v 'drawable=' appfilter_modified.xml; echo "$drawables")

echo '</resources>' >> appfilter_organized.xml

#Removed unused files.
rm appfilter_modified.xml

# Display a message to the user indicating that the script has finished
echo "The script has finished generating the 'appfilter_organized.xml' file."
