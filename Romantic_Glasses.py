import sys
from sys import stdin

def test_case():
    # Declare global variables to modify them within this function
    global ptr, input_data
    
    # Read the number of elements in current test case
    n = int(input_data[ptr])
    # Move pointer to next position in input
    ptr += 1
    
    # Read the next 'n' numbers as a list of integers
    a = list(map(int, input_data[ptr:ptr + n]))
    # Move pointer past these 'n' numbers
    ptr += n
    
    # Initialize a set to track prefix sums, starting with 0
    st = set()
    st.add(0)
    
    # Flag to track if condition is met
    cond = False
    
    # Running sum of alternating additions/subtractions
    s = 0
    
    # Loop through elements (1-based indexing like C++ version)
    for i in range(1, n + 1):
        # For odd positions (1-based), add to sum
        if i % 2 == 1:
            s += a[i - 1]  # Adjust to 0-based index
        # For even positions, subtract from sum
        else:
            s -= a[i - 1]  # Adjust to 0-based index
        
        # Check if current sum exists in set
        if s in st:
            cond = True
        
        # Add current sum to set
        st.add(s)
    
    # Print result for this test case
    print("YES" if cond else "NO")

def main():
    # Declare global variables to share between functions
    global ptr, input_data
    
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    # Initialize pointer to start of input
    ptr = 0
    
    # Read number of test cases
    T = int(input_data[ptr])
    # Move pointer to first test case
    ptr += 1
    
    # Process each test case
    for _ in range(T):
        test_case()

# Standard Python idiom to execute main() when run directly
if __name__ == "__main__":
    main()