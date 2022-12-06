#!bin/bash

#run: test1.sh my_argument

#-------------------------
echo Hey! press enter to continue
#Use 'read' to get user input
read
echo Thanks!

#-------------------------
# read external variable file
#dot + space means 'source' - in this case pulling in data or code from another file
. myvars
#Alternatively, just use 'source'
source myvars

echo "the color we have is: ${COLOR}"

#-------------------------
# $1 gets the value of the first argument given to the script
echo "the argument you gave is: ${1}"

#-------------------------
# "$@" gets ALL arguments- so this is a for loop printing out all arguments
# There are other ways to do this, like "$*" but there are advantages to "$@"
# Also, "$#" prints out the number of arguments!
for i in "$@"
do
    echo $i
done

#-------------------------
echo $(date +%Y-%m-%d)

#-------------------------
#Create file with no content IF IT DOES NOT ALREADY EXIST (no overwrite)
touch ./$(date +%Y-%m-%d)