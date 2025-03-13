def get_book_text(file_path):#Function to get bookinput as string
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_number_words(s):#Function to return number of words in string
    res = s.split()
    return len(res)


def get_letter_count(s):#Function that returns a dict where each key is a letter and each value the times it has occured in input string
    res = {}

    for l in s:
        l = l.lower()
        if l.isalpha(): #Check if character is a valid letter
            if l not in res:
                res[l] = 1
            else:
                res[l] += 1
    return res


def sorted_dicts(dict): #Sort dictionary to a list with dicts that have 2 keys, char and count
    res = []

    for key, value in dict.items():
        res.append({'char': key, 'count': value})

    res.sort(reverse = True, key = lambda dict: dict['count'])

    return res

