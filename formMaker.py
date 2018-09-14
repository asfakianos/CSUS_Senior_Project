# formMaker.py
# Alexander Sfakianos
# May 17, 2017

import datetime
import os


def makeForm(surveyTitle, Q, ID):
    """Creates the initial <form> tag and appends questions til end."""
    # Creates the tag for the form
    form = '\t<form action="/{}.php" method="post">\n'.format(surveyTitle)

    # Iterates through each question and its respective ID
    for num in range(len(Q)):
        form += addForm(Q[num], ID[num])

    form += endForm()
    return form

def addForm(Q, ID):
    """Takes a question string 'Q' and converts it to a form tag. ID is an
identifier for each question."""
    # Adds the question to the string
    form = "\t\t" + Q
    # Adds the tag + ID for PHP
    form += '<input type="text" name="{}"><br>\n'.format(ID)

    return form

def endForm():
    """Adds the last tags for the form, ends."""
    # First tag creates a submit button, second tag closes the initial form tag
    form = '<br><hr><br>\t\t<input type="submit">\n\t</form>'

    return form

def makePHP(surveyTitle, fileID, data, ID, newFolder, spacers):
    """Creates a .php file with the given parameters to connect it to the
HTML file"""
    # Read the file (PHPtemplate.txt)
    with open('PHPtemplate.txt', 'r') as file :
        filedata = file.read()

    # Replace the target strings...
    # Variables
    filedata = filedata.replace('!!varAndID', definePHPVar(ID))
    # IP
    filedata = filedata.replace('!!getUserIP',
                                "$IP = $_SERVER['REMOTE_ADDR'];\n" +
                                "\t\tfwrite($myfile, $IP);\n" +
                                '\t\tfwrite($myfile, "\t*!^*!\t");\n')
    # File Name
    filedata = filedata.replace('!!fileNAME', surveyTitle + fileID + ".dat")

    # Get all of the code necc. to acquire variables in PHP
    getVars = ""
    for a in ID:
        getVars += getPHPVar(a)

    # Add the variable-getting code to the PHP file.
    filedata = filedata.replace('!!addVARIABLESHERE', getVars)

    # Create the file name
    target = surveyTitle + ".php"

    with open(newFolder + "/" + target, 'w') as file:
        file.write(filedata)
        file.close()
    
def getPHPVar(varName):
    """Sets up the structure for getting a PHP variable from <form> based on
the given variable."""
    # Checking if the variable field is empty in the form.
    structure = ('\t\tif(empty(${})){}\n\t\t\t'.format(varName, '{') +
                 '${} =  "";\n\t\t{}\n'.format(varName, '}'))

    # Using *!^*! as a separator for variables.
    structure += ('\t\tfwrite($myfile, ${});\n'.format(varName) +
                  '\t\tfwrite($myfile, "\t*!^*!\t");\n')

    return structure

def definePHPVar(ID):
    """varNames List allows PHP to define all variables at once."""
    getVars = ""
    for i in range(len(ID)):
        getVars += "\t\t${} = $_REQUEST['{}'];\n".format(ID[i], ID[i])

    return getVars

def makeData(surveyTitle, random, name, path, desc):
    """Creates a .txt file to serve as the data storage for the corresponding
form."""
    # Name of the target data file.
    data = surveyTitle + random + ".dat"

    # Write to the new file
    with open(path + "/" + data, 'w') as dataFile:

        # Creating a header for the data file
        today = str(datetime.datetime.now()).split(" ")

        # Creating a header
        dataFile.write(str(surveyTitle) + "\n")
        dataFile.write(desc)
        dataFile.write('\nCreated on {} by {}.\n\n\n'.format(today[0], name))

        dataFile.close()

    return data
