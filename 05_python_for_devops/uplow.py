#!/usr/bin/env python3
string_entered = input("Please enter a string: ").strip()
stride = int(input("Please enter a stride: ").strip())
string_len = len(string_entered)

end_value = 0
start_value = 0
stop_value = stride
word = ''

while end_value <= string_len:
    word += string_entered[start_value:stop_value].upper()
    start_value += stride
    stop_value += stride
    end_value += stride

    word += string_entered[start_value:stop_value].lower()
    start_value += stride
    stop_value += stride
    end_value += stride

print(word)
