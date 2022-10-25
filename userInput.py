""" 
Anthony Beltran
CS 361 program to test microservice, microservice.py,  of Garrett Crowley's POS Project
October 24, 2022
"""
from array import array
import sys
from time import sleep
def main():
    """ 
    This program writes a total the total.txt file that is used by microservice to read 
    from and calculate gratuity and write to another file.
    """
    while True:
        # Enter total or quit
        total_original = input("Enter total or 'quit' to quit: ")
        if total_original != "quit":
            # code to write bad input to total.txt
            file_with_total = open('total.txt', 'w')
            file_with_total.write(total_original)
            file_with_total.close()
            
            print("Number written to total.txt:",total_original)

            """
            # code that only allows good input to total.txt
            try:
                file_with_total = open('total.txt', 'w')
                number = round(float(total), 2)
                print(f"Number written to total.txt: {number}")
                #os.write(file_with_total, str(number))
                file_with_total.write(str(number))
                #file_with_total.flush()
                #os.fsync(file_with_total)


                print(f"{number} written to total.txt")

                file_with_total.close()
            except:
                #print("Invalid input")
                #sys.exit(1)
                continue
            """


        else:
            break
        array_Total = []
        file_with_gratuity = open('gratuity.txt', 'r+')
        total = file_with_gratuity.read().splitlines()
        for line in total:
            array_Total.extend(line.split())
        if len(array_Total) !=3:
            print("waiting for data...")
            sleep(1)
            continue
        print("\nRecieving data..\n")
        try:
            print(f"{total_original}: gratuity of 10%: {float(array_Total[0])}\n")
            print(f"{total_original}: gratuity of 15%: {float(array_Total[1])}\n")
            print(f"{total_original}: gratuity of 20%: {float(array_Total[2])}\n")
        except:
            continue 
        array_Total = []   
        file_with_gratuity.truncate(0)
        file_with_gratuity.close()


if __name__ == "__main__":
    main()
