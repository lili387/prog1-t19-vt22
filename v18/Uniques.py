import re

# 1 downloaded from https://github.com/almgru/svenska-ord.txt/blob/master/svenska-ord.txt
# 2 downloaded from https://github.com/titoBouzout/Dictionaries/blob/master/Swedish.dic
swedish_dict_filename_1 = "svenska-ord.txt"
swedish_dict_filename_2 = "Swedish.dic.txt"

def read_dictionary_txt_as_list(filename):
    words = []
    with open(filename) as file:
        for line in file:
            line_content = line.rstrip().split("/")
            word_part = line_content[0].lower()
            if "-" in word_part or " " in word_part:
                continue

            is_only_alpha = re.match('^[a-zåäö]+$', word_part)
            if not is_only_alpha:
                print(f'found strange {word_part}')
                continue

            words.append(word_part)
    return words

word_list_1 = read_dictionary_txt_as_list(swedish_dict_filename_1)
word_list_2 = read_dictionary_txt_as_list(swedish_dict_filename_2)

unique_words = []

for word1 in word_list_1:
    if not word1 in word_list_2:
        unique_words.append(word1)
    
print(f'Found {len(unique_words)} unique words in list 1.')