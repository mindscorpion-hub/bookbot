def get_book_text(filepath):
        with open(filepath) as file:
            file_contents = file.read()
        return file_contents

def get_word_count(string):
        word_count = len(string.split())
        return word_count

def get_letter_count(string):
        letters = {}
        lower_letter = string.lower()

        for letter in lower_letter:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1

        return letters

def letter_format(dict):
        dict_list = []
        for i in dict:
            dict_list.append({"char":f"{i}", "num":dict[i]})
        return dict_list

def sort_on(items):
        return items["num"]

