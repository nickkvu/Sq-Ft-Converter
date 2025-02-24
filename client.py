import time

# Interface for Mircoservice A: Sq-Ft to Sq-M Converter
# 
# Functional Requirments:
#
# (1) Given a user is on the sq ft to sq meters converter, when the user enters a sq ft value, then the sq meters equivalent value is then outputed
# to the interface.
#
# (2) Given a user is on the sq ft to sq meters converter, then the users a non-number value, then the interface will return an INVALID prompt 
# and request the user to re-enter the input.
#
# (3) Given a user is on the sq ft to sq meter converter, when the user selected the process multiple input option, then the user should enter multiple values 
# and display a list of conversion.

if __name__ == "__main__":
    # get the input from the user to determine if the user wants to enter a single number or multiple numbers
    user_input = input("Press '1' to enter a single conversion or press '2' to enter multiple conversions: ").strip().lower()

    if (user_input == "1") :
        # error handling to validate if the user has entered a valid value (make sure value is non-negative and is a int or decimal)
        while (True) :
            # get the VALID Sq-ft number from the user to send it to the converter
            value = input("Enter sq.ft value: ")
            try :
                num = float(value)
                break   # break the error handling loop if user successfully enters valid value
            except ValueError :
                print("Invalid value")

        # write to the pipe.txt file to proceed with the single input process
        with open("pipe.txt", "w", encoding="utf-8") as f :
            f.write("single\n" + value)     # write the type of operation and the user value(s) to the pipe comm file
            
        print("Connecting to server...")
        time.sleep(3)   # ensures proper reading of the pipe.txt file using a "buffer"
        
        # wait on the Mircoservice A
        print(f"Requesting conversion for {value} sq.ft")
        while (True) :
            with open("pipe.txt", "r") as f :
                result = f.read().strip()
                print(f"Received data: {result} sq.m")
                break
            time.sleep(0.5)
        

    elif (user_input == "2") :
        # write to the pipe.txt file to proceed with the multiple entry process
        # first ask user to enter how many inputs they wish to enter in a row
        size = input("How many conversions would you like to make (in a row): ").strip().lower()
        size_num = int(size)
        input_list = []

        for i in range(size_num) :
            while (True) :
                # get the VALID Sq-ft number from the user to send it to the converter
                value = input("Enter sq.ft value: ")
                try :
                    num = float(value)
                    break   # break the error handling loop if user successfully enters valid value
                except ValueError :
                    print("Invalid value")
            # add the valid input to the list
            input_list.append(float(value))
        
        # once the list has been fully populated then write list to the pipe.txt file
        with open("pipe.txt", "w", encoding="utf-8") as f :
            f.write("multiple\n")     # write the type of operation and the user value(s) to the pipe comm file
            for num in input_list :
                f.write(f"{num}\n")
        
        print("Connecting to server...")
        time.sleep(3)   # ensures proper reading of the pipe.txt file using a "buffer"
        
        # wait on the Mircoservice A
        print(f"Requesting multiple conversion for the entered list")
        while (True) :
            with open("pipe.txt", "r") as f :
                print(f"Received list data\nConversions:")
                results = f.readlines()
                for num, result in zip(input_list, results) :
                    print(f"{num} sq.ft --> {result.strip()} sq.m")
                break
            time.sleep(0.5)
