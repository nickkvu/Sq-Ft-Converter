# Sq-Ft-Converter (Microservice A)

## How to Request Data from Microservice A
Using text files as the **communication pipe**, you must write the arguments/parameters to request data from the microservice to the **pipe.txt** file.

### Making Single Conversion
To convert one value from Sq.ft to Sq.m, the pipe.txt file must have **2 arguments** separated by each line: process type and input.

1. Using the UI/client program, the user will be prompted to enter a VALID value to send to the microservice. A VALID value is any whole or decimal number, it allows the value to be negative as well.<br/><br/>

Code snippet for data request of single conversion:
  ![Example data request for single conversion](images/microa-single-1.png) <br/><br/>
  
Example in UI: The user wants to get a single conversion for 100 Sq.ft
  ![Terminal view of data request for single conversion](images/microa-single-2.png) <br/><br/>

2. The client program should have sent 2 lines to the pipe.txt file to indicate that this is a single conversion process request

Example pipe.txt content for the request of a single conversion for 100 Sq.ft
![pipe.txt content for single conversion request example](images/microa-single-3.png) <br/><br/>

### Making Multiple Conversions


## How to Receive Data from Microservice A
