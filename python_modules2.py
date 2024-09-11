# Question 2: Mastering Python Modules and Aliases

# Task 1: Custom Module with Aliases 

from text_utils import reverse_string as rev_st, capitalize_string as cap_st

def reverse_capitalize():
    while True:
        try:
            s = input("\nWhat words would you like to reverse, and then capitalize? Enter words here: ").title()
            print(rev_st(s))
            print(cap_st(s))
        except Exception as e:
            print(f"An unexpected error {e} occured. Please try again.")
    
reverse_capitalize()
    