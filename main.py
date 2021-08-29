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

    # remove extra whitespaces
    string = ' '.join(string.split())

    return string


def find_table_names(string):
    table_names = set()

    # find next closest 'from ' or 'join '
    # take tablename after it assuming it isn't '('

    while string.find('from ') > -1 or string.find('join ') > -1:
        # find next closest 'from ' index
        next_from_index =  float('inf')
        if string.find('from ') > -1:
            next_from_index = string.find('from ')

        # find next closest 'join ' index
        next_join_index = float('inf')
        if string.find('join ') > -1:
            next_join_index = string.find('join ')

        # find the next closest keyword in string
        # i.e. the one with the smallest index
        next_keyword_index = min(next_from_index, next_join_index)

        # set remaining string to be slice
        # starting after next 'from ' or 'join ':
        string = string[next_keyword_index + 5:]

        # find index of next whitespace in remaining string:
        next_space_index = string.find(' ')

        # save table_name as slice from start of
        # remaining string until next whitespace
        table_name = string[:next_space_index]

        # set remaining string as slice starting
        # after end of table_name
        string = string[next_space_index:]

        # if the table_name isn't the start of
        # a subquery, save it to table_names
        if table_name != '(':
            table_names.add(table_name)

    return list(sorted(table_names))


#  this function assumes that the .sql file does not have any syntax errors:
def find_table_names_from_sql_file(file_name):
    string = process_sql_file(file_name)
    table_names = find_table_names(string)
    return table_names


if __name__ == '__main__':
    print(find_table_names_from_sql_file('file.sql'))