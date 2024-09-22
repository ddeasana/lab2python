def derive(A, B):
    if not isinstance(A, int) or not isinstance(B, int):
        return "Error: A and B must be integers."
    if A < B:
        return list(range(A, B + 1))  # Ascending
    else:
        return list(range(A, B - 1, -1))  # Descending

try:
    A = int(input("Enter an integer for A: "))
    B = int(input("Enter an integer for B: "))
    result = derive(A, B)
    print(result)
except ValueError:
    print("Error! Please enter integers for A and B.")
