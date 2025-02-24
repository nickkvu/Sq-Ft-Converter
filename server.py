import time

def sq_ft_to_sq_m_converter(val) :
    return round(float(val * 0.092903), 3)    # 1 sq.ft = 0.092903 sq.m


# Microservice A Implementation: Sq-Ft to Sq-M Converter
if __name__ == "__main__":
    while (True) :
        time.sleep(1)   # sleep of 1 second for some "buffer" time before reading the pipe.txt file

        # open the pipe.txt file to see if any commands/parameters have been sent to the file
        with open("pipe.txt", "r") as f :
            content = f.read().splitlines() # splits on newlines (basically strtok() on '\n') and makes a list 
        
        # start the program if there are commands/parameters in the file
        if content :    # check to see if content is empty or not
            if (content[0] == "single") :
                print(f"Receiving {content[0]} conversion for: {content[1]} sq.ft")
                with open("pipe.txt", "w", encoding="utf-8") as f :
                    result = sq_ft_to_sq_m_converter(float(content[1]))
                    f.write(f"{result}\n")  # write to the pipe.txt fule
                    print(f"{result} was written to pipe.txt")
            
            if (content[0] == "multiple") :
                print(f"Receiving {content[0]} conversions for provided list: ")
                with open("pipe.txt", "w", encoding="utf-8") as f :
                    for line in content[1:] :
                        result = sq_ft_to_sq_m_converter(float(line))
                        f.write(f"{result}\n")
                print("Converted list was written to pipe.txt")
        
        time.sleep(1)