import urllib
import requests

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    #Split book into words and save each words to the array. Be careful not to also record exclamation marks.
    pass
# If you are given an array of numbers as the input to apply a radix sort, the algorithm is to:
# 1. Initialize two arrays called the output and count arrays.
# 2. Get the maximum digit from your input array and use the number of digits in the maximum number to know how many rounds of counting sort to perform.
# 3. Beginning from the unit or ones position, count the frequency of each digit. Do this for all place values. If the maximum number has 4 digits,
#    you will do this for the ones, the tens, the hundreds and the thousands place value. So you will have 4 rounds of counting sort.
# 4. Count the occurrences of each digit and store each count in the count array.
# 5. Convert the counts to prefix sums. This basically means that you should add each number to its predecessor and the sum should replae the number.
#    essentially this means that if you have 1,2,4,6,4,3,2,2,5,9,5,7, performing a prefix sum would yield, 1,3,7,13,17,20,22,24,29,38,43,50.
# 6. Build the output from the prefix sums. Based on the place value you counted the occurrence of each digit for, you will start from the right hand side
#    of the input array and using the place value just accounted for, place the number in its respective slot in the output array. This is done by
#    tracing the digit to its corresponding prefix sum (count array) index and then taking the number at that index slot, subtracting one from it
#    and using it as the index slot where you will place the input number in question in the output array.
# 7. Copy the output to the input array.
# 8. Zero all the counts in the count array in preparation for subsequent rounds.

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def set_string_length (unsorted):
    # This method aims to use the * character to make all the strings to be sorted as long as the longest one.
    maxSize = 0
    for word in unsorted:
        if len(word) > maxSize:
            maxSize = len(word)
    
    sameLengthWords = []
    for word in unsorted:
        arr = ['*' * (maxSize - len(word))]
        sameLengthWords.append(word.lower() + ''.join(arr))
    return sameLengthWords

def read_in_words (book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass