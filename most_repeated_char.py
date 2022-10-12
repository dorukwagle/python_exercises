def char_frequency(string):
    counter = {}
    #first get the occurance of every letter in the sentence
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter.items()

def most_repeated_method1(string):
    #now loop through the dictionary and get the highest repeated number
    frequency = char_frequency(string)
    highest = list(frequency)[0]
    for key, value in frequency:
        if highest[1] < value:
            highest = key, value
    return highest
    
    
def most_repeated_method2(string):
    #first sort the given frequency list
    frequency = char_frequency(string)
    frequency = sorted(frequency, key = lambda item:item[1])
    return frequency[-1]

string = "This is the most asked common interview question iiiiiiiiii, and is the is of in in iin iiin are different"
print("highest repeated: ", *most_repeated_method2(string))
        
