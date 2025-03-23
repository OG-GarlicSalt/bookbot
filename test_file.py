print("Step 1: Basic print test")

print("\nStep 2: Testing file opening")
try:
    with open("books/frankenstein.txt", "r") as f:
        first_few_chars = f.read(100)
    print(f"First 100 characters:\n{first_few_chars}")
except Exception as e:
    print(f"Error opening file: {e}")

print("\nStep 3: Test complete")
