
while True: # make the program to continuous loop, 
   
    user_input = input("Enter any value: ")  # input , kung anong gustong ilagay nang user

    
    if user_input == "": # kung ang user ay walang nilagay input
        data_type = "NOTHING" # ito ay mag sasabi nang "You entered nothing" kapag ang user ay walang nilagay sa input
    elif user_input.isdigit():  # kung gagamit ng isdigit() para sa mga combination nang letters at numbers, at ito ay magiging "string" 
        data_type = "Integer"   # kung puro numbers naman ang na input nang user , mag sasabi ito nang integer
    elif any(char.isdigit() for char in user_input) and any(char.isalpha() for char in user_input): # kung ang user ay nag input ng combination ng letters at numbers
        data_type = "Combination of numbers and letters, it is 'string'"
    elif any(char.isalpha() for char in user_input) and any(not char.isalnum() for char in user_input): #kung ang user ay nag input ng combination ng letters at special characters
        data_type = "Combination of letters and special characters, it is 'string'" 
    elif (any(char.isdigit() for char in user_input) and 
          any(not char.isalnum() and char != '.' for char in user_input)): #kung ang user ay nag input ng combination ng special characters at numbers
        data_type = "Combination of numbers and special characters, it is 'string'"  
    else:                       
        try:                    # kung ang input sa taas ay hindi ma convert, mag eexecute ang nakapaloob sa try statement.
            float_value = float(user_input)  # float para sa mga nag input nang may decimal point
            if '.' in user_input:  
                data_type = "Float"     #ito ay para sa may decimal point
            
            else:
                data_type = "Integer"    # ito ay para sa mga walang decimal point

        except ValueError:             # except para sa maling input nang user, mag eexecute sa "string" 
                                        #ValueError para maiwasan ang pag crash nang program at ito ay magsasabi nang string 
                                            #para sa lahat nang combination ng numbers,letters at mga special characters
            data_type = "String" 

    
    print(f"You entered {data_type.lower()}.") # ipiprint ang laman nang data_type sa lower case

   
    while True:     # second continuous loop inside the first loop
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()  # ito ay para naman kung itutuloy ang program o hindi na, .strip() para tanggalin ang extra space
        if try_again in ['yes', 'y']: # kung ang user ay pumili nang nang "yes", "y" ito ay babalik sa first loop
            break                   # break para bumalik sa first loop
        elif try_again in ['no', 'n']: # kung ang user ay sumagot nang "no", "n" , mag sasabi na nang Goodbye
            print("Goodbye!")
            exit()  # para tapusin ang loop code
        else:
            print("Invalid input, please respond with 'yes' or 'no'.") # kung ang user ay hindi pumili sa yes or no , ito ay magsasabi na respond with yes or no.
