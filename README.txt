CS 361 Microservice for Garret Crowley's POS



Communication is through text files
    a. total.txt
    b. gratuity.txt

### Request Data ###

The microservice continuosly tries to read data from 
total.txt, which a program would write the total in. The microservice
does not try to calculate bad data such as strings or a total with 
more than one number.
The microservice clears the bad data and continues to 
wait for acceptable data in total.txt.

### Recieve Data ##
The microservice calculates the gratuity of 10%, 15%, and 20%.
These numbers are written to the file, gratuity.txt.
A program would read the calculated results from total from 
the gratuity.txt file.

Summary:
A program requests data by writing a total in total.txt. 
The microservice reads this total. 
The microservice calculates the gratuity from recieving 
the total data and writes this to gratuity.txt.
The program reads gratuity.txt and recieves the data.

The microservice ignores the total.txt if it's empty, not a number or
there is more than one number in the file. 
The sleep() functions were for debugging and could 
be removed after integration and working code.





### UML ###

