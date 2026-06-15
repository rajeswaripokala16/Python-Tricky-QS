import time

password = input("Enter Password: ")

start = time.time()

chars = "abcdefghijklmnopqrstuvwxyz"
guess = []

for val in range(5):               # try passwords up to length 5
    # start from all 1‑char strings
    a = [c for c in chars]
    for _ in range(val):
        # build all strings of length val+1
        a = [x + c for x in a for c in chars]
    guess += a
    if password in guess:
        break

end = time.time()
clock = str(end - start)

print("Your password: " + password)
print("Time taken: " + clock)
