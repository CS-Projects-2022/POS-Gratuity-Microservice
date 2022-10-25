""" 
Name: Anthony Beltran
October 24, 2022
CS 361 Microservice
This program is a microservice to go with Garret Crowley's project 
"""
import string
import sys
from time import sleep


def main():
    """ 
    This program calculates 10% 15% and 20% from total
    read from total.txt and writes the three numbers to gratuity.txt.
    This while loop is a continuous while loop if variable = False is commented out
    This program reads from total.txt and clears it.
    If there is only one number it writes the calculations to gratuity.txt
    if total.txt is empty, continue
    """
    variable = True
    count = 0
    MAXTOTAL = 10000000
    while variable:

    
        # Open total.txt
        array_Total = []
        gratuity_A = []
        
        file_with_total = open('total.txt', 'r+')
        #file_with_gratuity = open('gratuity.txt','w+')
        total = file_with_total.read().splitlines()
        for line in total:
            array_Total.extend(line.split())
        file_with_total.truncate(0)
        
        # Checking if array is empty and continue if it is empty
        # total is the value if it is not empty
        try:
            total = array_Total[0]
            count = 0
        except:
            print("file is empty")
            count+=1
            #sleep(3)
            #file_with_gratuity.truncate(0)
            sleep(1)
            if count==20:
                break
            continue

        # we have total, but if there is more than one number in total.txt, something is wrong
        # continue if there is more than one number
        if len(array_Total) != 1:
            print("Error: input length is not 1")
            #sleep(3)
            #file_with_gratuity.truncate(0)
            #file_with_gratuity.close()
            count += 1
            sleep(1)                        # Change when integrating
            
            if count == 10:                  # Change when integrating
                count = 0
                break
            continue


        """"
        elif not total.isnumeric():
            print("its not a number")
            count += 1
            sleep(1)
            
            if count == 5:
                count = 0
                break
            continue
        """
        # try converting total into float if its a number, if not, continue
    
        try:
            total = float(total)
            if total > MAXTOTAL:
                count += 1
                continue
            count = 0
        except:
            print(f"NAN-type is: {type(total)}")
            count += 1
            #sleep(3)
            #file_with_gratuity.truncate(0)
            sleep(1)                              #change when integrating
            if count == 10:
                break
            continue
        file_with_total.close()
        ten = .10 * total
        ten = round(ten,2)
        
        fifteen = .15 * total
        fifteen = round(fifteen,2)
    
        twenty = .20 * total
        twenty = round(twenty,2)
        print(f"Good input length: {len(array_Total)}")
        
    
        #total = float(total)
        #print(total)
       
        with open('gratuity.txt','w') as output:
            for i in range(3):
                if i==0:
                    output.write(str(ten)+'\n')
                    print(f"10% written to file: {ten}")
                elif i==1:
                    output.write(str(fifteen)+'\n')
                    print(f"15% written to file")
                else:
                    output.write(str(twenty)+'\n')
                    print(f"20% written to file: {twenty}")
        
        output.close()
    # comment out if you want the loop to be continuous    
    variable = False
    return
        
            
    
    

        
        
    """  
        number = round(float(total), 2)
        print(f"Number written to gratuity.txt: {number}")
        #os.write(file_with_total, str(number))
        file_with_total.write(str(number))
        #file_with_total.flush()
        #os.fsync(file_with_total)


        print(f"{number} written to gratuity.txt")

        file_with_total.close()
    """        

if __name__ == "__main__":
    main()