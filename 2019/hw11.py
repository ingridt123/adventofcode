

GAP = "_" # This is the character we choose to show gaps.

ALIGN = "|" # This is the character we choose to show alignmed characters.


def showAlignment(x, y, method_name):
    ''' show the alignment of x and y using whichever method is named                      '''
    ''' We build a procedure call symbolically using the name of the method, then eval it. '''
    # command = method_name + "('" + str(x) + "', '" + str(y) + "', '" + str(GAP) + "')"
    command = method_name + "('" + str(x) + "', '" + str(y) + "')"
    print('\n' + command)
    result = eval(command)
    print("raw result = " + str(result))
    if result == None:
        print("\n*** Test failed on aligning " + x + " with " + y + " using " + method_name)
    else:
        (u, v, n) = result
        print(u)
        for i in range(0, min(len(u), len(v))):
            if u[i] == v[i]:
                print(ALIGN, end = '')
            else:
                print(" ", end = '')
        print("\n" + v)
        print("llcs = " + str(n))
        print("")
        
import random    # for generating random bit strings for testing

# Generate some long strings for testing
def randomBitString(n):
    result = ""
    for i in range(0, n):
        result += ('1' if random.random() > 0.5 else '0')
    return result

xbits = str(randomBitString(80))
ybits = str(randomBitString(80))

def tests(method_name):
    ''' Run test cases using the given method name '''
    print("\n*** tests using " + method_name + " ***")
    showAlignment('ATTGC', 'GATC', method_name)
    showAlignment("GCGCAATG", "GCCCTAGCG", method_name)
    showAlignment("HarveyMudd", "HarvardMed", method_name)
    showAlignment("GTACGTCGATAACTG", "TGATCGTCATAACGT", method_name)
    showAlignment("CATTAGATATAGACG", "CTATAGATATAGGGC", method_name)
    showAlignment("AGGCTATCACCTGACCTCCAGGCCGATGCCC", "TAGCTATCACGACCGCGGTCGATTTGCCCGAC", method_name)
    showAlignment(xbits, ybits, method_name)
    showAlignment("AAACCGTGAGTTATTCGTTCTAGAAAAACGGTGGGAGTCACAGAT", 
                    "CACCCCTAAGGTACCTTTGGTTCTGATCGTCATAACGT", method_name)

def main():
    # tests("align_c")
    # tests("align_d")
    tests("align_caching")
    tests("align")

main()


# print(llcs("GTACGTCGATAACTG", "TGATCGTCATAACGT") == 12)
# print(llcs("ABCDGH", "AEDFHR") == 3)
# print(llcs("AGGTAB", "GXTXAB") == 4)
# print(llcs("", "") == 0)
# print(llcs("ABCDER", "12930") == 0)

