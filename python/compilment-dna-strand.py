def complementary_strand_final(dna_strand):
 
    # empty string define
    complementary_strand = ""
 
    # looping through the
    # given DNA strand one
    # by one character at
    # a time 
    for base in dna_strand:
 
        # using if-elif-else
        # conditional statement
        if base == "A" :
            # string concatenation
            complementary_strand += "T"
 
        elif base == "T" :
            complementary_strand += "A"
 
        elif base == "G" :
            complementary_strand += "C"
 
        elif base == "C" :
            complementary_strand += "G"
 
        else :
            complementary_strand += "H"
            # break out of the loop
            # if any other input is given after printing H
            break
 
    # return final result
    return complementary_strand
 
# main code
if __name__ == "__main__":
 
    # input the DNA strand
    dna_strand = str(input())
 
    print("DNA strand is:",
          dna_strand)
 
    # function call and printing
    # the result
    print("complementary strand is:",
          complementary_strand_final(dna_strand))
