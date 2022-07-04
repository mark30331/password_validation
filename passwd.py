def check_for_uppercase(password):    
    return any(i.isupper() for i in password)

def check_for_lowercase(password):    
    return any(i.islower() for i in password)

def check_for_number(password):  
    return any(i.isdigit() for i in password)

def check_for_special(password):
    special_char = ["@" ,  "#" , "%", "-", "&", "*"]
    return any(i in special_char for i in password)

def main():
    print("Beginning password analysis…")
    try:
        f = open("Invalid.txt","w")
    except Exception as e:
        print("could not open Invalid.txt")

    try:
        v = open("valid.txt","w")
    except Exception as e:
        print("could not open valid.txt")

    try:
        with open("Pwd.txt","r") as myfile:
            print("Opening file 'Pwd.txt'.")

            for line in myfile:    #  &&            
                if len(line) > 7 and check_for_lowercase(line) and check_for_uppercase(line) and check_for_special(line) and check_for_number(line):
                    v.write(line)
                    continue   
                f.write(line)
                                
    except Exception as e:
        print("File corrupted or Does not exit")
    myfile.close()
    v.close()
    f.close()

    print("Analysis complete. Closing files.")

main()