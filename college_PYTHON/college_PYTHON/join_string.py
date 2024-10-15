def string(input):
    word=input.split()
    return word
def join_word(join_w):
    join_string=' '.join(join_w)
    return join_string

user=input("enter any string: ")
string_in=string(user)
word_join=join_word(string_in)
print(f"list of word is:{string_in}")
print(f"join word is:{word_join}")