def word_frequency_counter(text):
    # Create an empty dictionary to store word frequencies
    word_freq = {}
    
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Iterate through the words and count frequencies
    for word in words:
        # Remove punctuation from each word
        word = ''.join(char for char in word if char.isalnum())
        
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq


input_text = "Hello world! Hello everyone. World, hello!"
word_count = word_frequency_counter(input_text)
print(word_count)
 