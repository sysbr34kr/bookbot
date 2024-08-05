# Load book into code
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# Counts how many words
def word_count():  
    words = file_contents.split()
    count = len(words)
    print(f"Number of words: {count}")
    
def sort_on(dict):
    return dict["count"]

# Counts how many characters
def character_count():    
    lower_case = file_contents.lower()
    character_dict = {}
    
    for i in lower_case:
        if i.isalpha(): # Counts only alphabetic characters
            if i in character_dict:
                character_dict[i] += 1
            else:
                character_dict[i] = 1
    
    # Creates a list of dictionaries and sorts them
    character_list = []
    for j, k in character_dict.items():
        character_list.append({"char": j, "count": k})
    character_list.sort(reverse=True, key=sort_on)
    
    # Prints the list in a more organized manner
    for h in character_list:
        print(f"The {h['char']} character was found {h['count']} times")

print("--- Begin Report ---")
word_count()
character_count()
print("--- End Report ---")