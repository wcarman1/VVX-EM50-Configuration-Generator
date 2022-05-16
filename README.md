# VVX-EM50-Configuration-Generator

A tool for creating Metaswitch import files for the VVX EM50 expansion modules.

How to use:
Create a .csv file with the key number in column A and directory number in column B. **Key numbers for the vvx em50 start at 23 and go up to 112 so start at 23**
See exampleSidecar.csv for an example of the file. **column C isn't used to create the import file it's just there to make it easier to arange the keys**
Fill in the csv file with the extensions making sure to put them in the order you'd like them to appear on the EM50.

Run the Main.py file

Click input file and select the CSV you just created
Creat a file that you'd like to save the import information to. Right click on your desktop > create new > Text document
Click output File and select the text file you just created
Click Create Configuration

Open the output file in a text editor and make sure the xml configuration is present

Open MVW and navigate to the VVX 450 phone profile you'd like to import to.

If it doesn't have an EM50 currently click add sidecar and then save changes

Click import > Keep current settings > Select the .txt file with the xml configuration in it

Let it import and make sure the changes were successful

Check the key assignment (should be highlighted in blue indicating new unsaved settings)

If correct, click Save changes. If incorrect, click Discard Changes.
