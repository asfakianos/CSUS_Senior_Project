# htmlWriter2.py
# Alexander Sfakianos
# May 17, 2017

import formMaker
import random
import os

def isSafe(test):
    """Ensures that the question has no text that could damage file
(comments, etc)."""
    # A list of potentially dangerous characters.
    danger = ["#", "<", ">", "/", "*", '\n', '\t', '%', '|', '@']

    for letter in test:
        if letter in danger:
            # If a single character is 'dangerous', return unsafe.
            return False

    # If it makes it through the entire string, safe.
    return True

def getNames(prompt):
    """Gets a string for the requested string. Pass prompt as a string to
prompt the user"""
    string = ''

    while string == "":
        try:
            string = input(prompt)
            if not isSafe(string):
                raise TypeError
            else:
                return string

        except:
            string = ""
            print('That is an invalid response, please try again.')

def getUserNo():
    """Gets the necessary info before beginning."""
    qs = ""
    surveyTitle = getNames("Please give a name for the survey:")
    header = getNames("Please give a header for survey:")

    while qs == '':
        try:
            qs = eval(input('Number of questions:'))

        except:
            print('Please give a valid number')
            qs = ''

    return qs, surveyTitle, header

def getUserQ(qs, surveyTitle):
    """Gets the questions that the user wishes to ask."""
    Q = []
    ID = []

    # Iterates -- gets questions based on provided length
    for prompt in range(qs):
        print('Question no.' + str(prompt + 1) + ':')

        # Adds the question to list 'Q'
        Q.append('<hr>' + input('') + '<br>')
        ID.append(surveyTitle[0] + str(prompt))

    return Q, ID

def htmlCreate(surveyTitle, header, form, random, desc, name):
    """Creates a new file with the provided info."""
    newFolder = 'D:/Desktop/Senior Project/{}'.format(surveyTitle +
                                                      " " + random)
    os.makedirs(newFolder)
    
    # Read the file (template.txt)
    with open('HTMLtemplate.txt', 'r') as file :
        filedata = file.read()

    # Replace the target strings
    # Webpage Title
    filedata = filedata.replace('surveyTitle', surveyTitle)
    # Survey Header
    filedata = filedata.replace('surveyHeader', header)
    # Adding in the form
    filedata = filedata.replace('surveyForm', form)
    # Survey description
    filedata = filedata.replace('surveyInfo', desc)
    # Footer fill-ins
    filedata = filedata.replace('!!writtenBy', name) 

    # Create the file name
    target = surveyTitle + ".html"

    # Write the file out again. In most cases, creates the file.
    with open(newFolder + "/" + target, 'w') as file:
        file.write(filedata)
        file.close()

    return newFolder

def main():
    spacer = '"\t*!^*!\t"'

    name = str(getNames("What's your name?")).title()

    # Getting the number of questions
    qs, surveyTitle, header = getUserNo()
    # Getting a description for the survey
    desc = getNames('Please give a description for the survey.')
    # Getting the questions
    Q, ID = getUserQ(qs, surveyTitle)
    # Creates a random 6-digit file ID to prevent overwrites
    fileID = str(random.randint(100000, 999999))

    # Converting the questions into an html form setup
    form = formMaker.makeForm(surveyTitle, Q, ID)

    # Creates the html File
    newFolder = htmlCreate(surveyTitle, header, form, fileID, desc, name)
    # Creates the data File, data is the name of the file.
    data = formMaker.makeData(surveyTitle, fileID, name, newFolder, desc)
    # Creates the PHP File
    formMaker.makePHP(surveyTitle, fileID, data, ID, newFolder, spacer)

    print('Files created. Check {}'.format(newFolder))


main()
