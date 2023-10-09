#chapter 2, number 14
#compound interest 

# A = P * (1 + r/n) ** (n*t)

# where P = the principle (initial value)
# r = the interest rate
# n = the number of terms
# t = the length of each term
def check_for_zero_values(principal_local_cfzv,rate_per_term_local_cfzv,applications_total_local_cfzv):
    if principal_local_cfzv == 0 or rate_per_term_local_cfzv == 0 or applications_total_local_cfzv == 0:
        zero_condition_local = True
        return zero_condition_local
    else:
        zero_condition_local = False
        return zero_condition_local

def calculate_interest(zero_condition_main, principal_local_cl,rate_per_term_local_cl,applications_total_local_cl):
    if zero_condition_main == True:
        print("---!!!---    Error! One or more critical values have been set to zero.  Double check your numbers.   ---!!!---")
        
    final_value_local_cl = principal_local_cl * ((1+rate_per_term_local_cl) ** applications_total_local_cl)
    return final_value_local_cl


        
        
def print_summary(principal_local_p, rate_local_p, number_of_applications_local_p, time_local_p, rate_per_term_local_p, applications_total_local_p, final_value_local_p):
    print("Summary:"
          "\nThe initial value of your cash was:",principal_local_p,"dollars."
          "\nThe rate provided was:",rate_local_p*100,"%"
          "\nThe rate was applied",number_of_applications_local_p,"times per term."
          "\n",time_local_p,"term(s) elapsed."
          "\n\nThe rate per term was",rate_per_term_local_p*100,"%"
          
          "\n\nThe rate was applied a total of",applications_total_local_p,"times."
          #round to three decimal places to avoid unnecessary digits 
          "\n\nAfter",applications_total_local_p,"terms, the value of your money is:",round(final_value_local_p,3),"dollars,")
    

def main():
    #input block
    principal_main = float(input("What is the intial amount of money you put in (in dollars)?"))
    rate_main = (float(input("What is the interest rate (as a percentage?)")) / 100)
    number_of_applications_main = int(input("How many times is the interest rate applied per term?"))
    time_main = int(input("How many terms elapse?"))
    #create individual variables to represent r/t, n*t

    rate_per_term_main= rate_main / number_of_applications_main
    applications_total_main = number_of_applications_main * time_main

    #run zero condition check
    zero_condition_main = check_for_zero_values(principal_main,rate_per_term_main,applications_total_main)
    #perform math and store in a variable If zero error, print to user
    final_value_main = calculate_interest(zero_condition_main, principal_main, rate_per_term_main, applications_total_main)
    
    #print a summary of the user's inputs and other relevant information. 
    print_summary(principal_main,rate_main,number_of_applications_main,time_main,rate_per_term_main,applications_total_main,final_value_main)

main()