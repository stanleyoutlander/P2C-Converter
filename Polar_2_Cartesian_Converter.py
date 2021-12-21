import getpass
import sys
import pandas as pd
import tkinter as tk
from tkinter import filedialog
sys.path.insert(0, './modules/fix/')
from illustratorfix import fix
from rotation import arot
sys.path.insert(0, './modules/converters/')
from p2cconvert import convert


if __name__ == '__main__':
    # Greet user
    print('Welcome, '+getpass.getuser() + '!')
    print('Polar 2 Cartesian Converter')
    print('Author: Wanda Sol')
    # Present "Open File Dialog" to choose CSV file
    root = tk.Tk()
    root.withdraw()
    # Define dataframe 'data' by filepath to CSV file
    maindata = pd.read_csv(filedialog.askopenfilename())
    # User choice if Illustrator fix is needed
    choice = input('Enter Y/Yes if you used raw Adobe Illustrator degrees for Polar.\n')
    if (choice == 'Y') or (choice == 'Yes'):
        print('Preparing DataFrame')
        fixdata = maindata['polar'].copy()
        print(fixdata)
        print('Applying Illustrator Fix...')
        polar = fixdata
        fixdata = fixdata.apply(fix)
        print(fixdata)
        print('Merging DataFrames')
        maindata['polar'] = fixdata.replace(maindata['polar'])
        maindata.reset_index(drop=False)
        print(maindata)
        print('Success!')
    else:
        pass
    # User choice if Y-Axis rotation is needed
    choice = input('Enter Y/Yes if you need to rotate Y-Axis for Polar.\n')
    if (choice == 'Y') or (choice == 'Yes'):
        print('Preparing DataFrame')
        rotdata = maindata['polar'].copy()
        print(rotdata)
        print('Applying rotation...')
        rot = maindata.iat[0, 0]
        rotdata = rotdata.apply(arot, args=[rot])
        print(rotdata)
        print('Merging DataFrames')
        maindata['polar'] = rotdata.replace(maindata['polar'])
        maindata.reset_index(drop=False)
        print(maindata)
        print('Success!')
    else:
        pass
    print('Preparing DataFrame')
    print(maindata)
    workdata = maindata[['polar', 'alpha', 'radius']].copy()
    print(workdata)
    print('Converting data... ;)')
    # Apply calculations and return XYZ Cartesian Coordinates for each row and write new data to new columns X, Y, Z
    workdata[['x', 'y', 'z']] = workdata.apply(convert, axis=1, result_type='expand')
    print(workdata)
    # Write DataFrame to CSV File
    workdata[['x', 'y', 'z']].to_csv(filedialog.asksaveasfilename())
    print('Success, check export.csv for your converted data ;)')
    print('Good luck with your Universe!')
