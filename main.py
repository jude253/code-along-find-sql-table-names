def process_sql_file(file_name):
    file, string = open(file_name, "r"), ''

    # for line in file, remove comments, space out '(' and ')', add line to output string:
    for line in file:
        line = line.rstrip()
        line = line.split('//')[0]
        line = line.split('--')[0]
        line = line.split('#')[0]
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        string += ' ' + line
    file.close()

    # remove multi-line comments:
    while string.find('/*') > -1 and string.find('*/') > -1:
        l_multi_line = string.find('/*')
        r_multi_line = string.find('*/')
        string = string[:l_multi_line] + string[r_multi_line + 2:]

    # remove extra whitespaces and make list
    words = string.split()

    return words


def find_table_names(words):
    table_names = set()
    previous_word = None

    for word in words:
        if previous_word == 'from' or previous_word == 'join':
            if word != '(':
                table_names.add(word)
        previous_word = word

    return sorted(list(table_names))


#  this function assumes that the .sql file does not have any syntax errors:
def find_table_names_from_sql_file(file_name):
    words = process_sql_file(file_name)
    return find_table_names(words)


if __name__ == '__main__':
    print(find_table_names_from_sql_file('file.sql'))