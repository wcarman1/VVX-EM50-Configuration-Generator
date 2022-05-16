import csv
from tkinter import *

# import filedialog module
from tkinter import filedialog


def creatconfig():
    inputfile = csv.reader(open(filename, 'r'))
    outputfile = open(filenameout, 'w')
    preconfig = """<!--
INFORMATION ABOUT THIS FILE

This export file includes all settings that have been explicitly configured at the scope being exported.
It does NOT include settings inherited from a higher scope, or any default settings.

Editing this file is not recommended and may lead to errors when trying to import.p
Please see https://communities.metaswitch.com/docs/DOC-275535 for information about SIP PS export files.
-->

<?xml version="1.0" encoding="utf-8"?>
<PhoneProfile xmlns="http://www.metaswitch.com/cp/clientxml" Identity="VVX_450" SequenceNumber="1" SIPPSVersion="2">
  <ProfileSettings>
"""
    postconfig = """    <ProfileSetting Identity="MetaswitchSidecars">VVX_EM50</ProfileSetting>
    <ProfileSetting Identity="SoftKeyPageGroup_40">1</ProfileSetting>
    <ProfileSetting Identity="SoftKeyMonitoredExtensionRingTone_40">Auto</ProfileSetting>
    <ProfileSetting Identity="SoftKeyMonitoredExtensionSpontaneousCallAppearance_40">Auto</ProfileSetting>
  </ProfileSettings>
</PhoneProfile>

<MetaDataFromExport>
  <MetaDataSetting ID=UserPrivilege>provider</MetaDataSetting>
  <MetaDataSetting ID=Scope>Subscriber</MetaDataSetting>
  <MetaDataSetting ID=PhoneModel>VVX_450</MetaDataSetting>
</MetaDataFromExport>"""

    outputfile.write(preconfig)

    i = 0

    for row in inputfile:
        if 0 < i < 112:
            key_number = row[0].replace(' ,', ',')
            ext_number = row[1].replace(' ,', ',')
            # print(key_number, ext_number)
            scconfig = f"""    <ProfileSetting Identity="MetaswitchSoftKeyAction_{key_number}">EnhancedMonitoredExtension</ProfileSetting>
    <ProfileSetting Identity="SoftKeyLine_{key_number}">Line1</ProfileSetting>
    <ProfileSetting Identity="SoftKeyXMLAppLine_{key_number}">1</ProfileSetting>
    <ProfileSetting Identity="SoftKeyDial_{key_number}"/>
    <ProfileSetting Identity="SoftKeyTransferDest_{key_number}"/>
    <ProfileSetting Identity="SoftKeyParkOrbit_{key_number}">MetaswitchNone</ProfileSetting>
    <ProfileSetting Identity="SoftKeyXMLApp_{key_number}">MetaswitchNone</ProfileSetting>
    <ProfileSetting Identity="SoftKeyMacro_{key_number}"/>
    <ProfileSetting Identity="MetaswitchSoftKeyLabel_{key_number}"/>
    <ProfileSetting Identity="SoftKeyExtension_{key_number}">{ext_number}</ProfileSetting>
    <ProfileSetting Identity="SoftKeyUseSubscriberNameAsLabel_{key_number}">Yes</ProfileSetting>
    <ProfileSetting Identity="UsePerMacroKeyState_{key_number}">false</ProfileSetting>
    <ProfileSetting Identity="MacroKeyStates_perMacro_{key_number}">idle</ProfileSetting>
"""
            outputfile.write(scconfig)
        i += 1
    outputfile.write(postconfig)
    label_file_explorer.configure(text="VVX EM50 Configuration wrote to: " + filenameout)


def browsefiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="%HOMEPATH%",
                                          title="Select a File",
                                          filetypes=(("Microsoft Excel Comma Separated Values File",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


def browsefilesout():
    global filenameout
    filenameout = filedialog.askopenfilename(initialdir="%HOMEPATH%",
                                             title="Select a File",
                                             filetypes=(("Text File",
                                                         "*.txt*"),
                                                        ("all files",
                                                         "*.*")))

    # Change label contents
    label_file_explorer.configure(text="Output File: " + filenameout)


# Create the root window
window = Tk()
# Set window title
window.title('VVX EM50 Configuration File Generator')

# Set window size
window.geometry("")
window.minsize(width=600, height=500)

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Select Input CSV and Output File Location",
                            width=100, height=4,
                            fg="black")

button_explore = Button(window,
                        text="Input File",
                        command=browsefiles)

button_exploreout = Button(window,
                           text="Output File",
                           command=browsefilesout)

button_run = Button(window,
                    text="Create Configuration",
                    command=creatconfig)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exploreout.grid(column=1, row=3)

button_run.grid(column=1, row=4)

# Let the window wait for any events
window.mainloop()
