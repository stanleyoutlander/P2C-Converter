# Importing libraries
import math
import pandas as pd
    
def p2cconvert(data):
    
    # Collect data for the calculator
    d = data.radius
    polar = data.polar
    alpha = data.alpha
    
    # Convert degrees into radians for polar and alpha arguments
    polar = polar * math.pi/180.0;
    alpha = alpha * math.pi/180.0;
    
    # Main calculation and output
    x = d * math.sin(polar) * math.cos(alpha)
    y = d * math.sin(polar) * math.sin(alpha)
    z = d * math.cos(polar)
    
    return x, y, z
    
if __name__ == '__main__':  
        
    # Read CSV file and collect data for DataFrame
    data = pd.read_csv('import.csv')
    
    # Apply calculations and return XYZ Cartesian Coordinates for each row
    data[['x','y','z']] = data.apply(p2cconvert, axis=1, result_type ='expand')
    
    # Write DataFrame to CSV File
    data.to_csv('export.csv')
    print('Success, check export.csv for your converted data ;)')  
