import time

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!"]

target = "im going to touch you"
phrase = [" "] * len(target)  # Start with a list of spaces

while "".join(phrase) != target:
    for i in range(len(target)):
        if phrase[i] != target[i]:  # Only update characters that don’t match
            ind = 0
            while phrase[i] != target[i]:
                phrase[i] = alphabet[ind]
                ind += 1
                print("".join(phrase))  # Print each time a character is changed
                time.sleep(.04)


