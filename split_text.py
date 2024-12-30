# str = "John|Jane|Doe|Smith|Emily|Michael|Sarah|David|Laura|Chris"

def split_text(my_str, separator):

    """"
    Function by Miguel Gutiérrez Fernández. 
    The following function takes a string and a separator as input and returns a list of strings. 
    The function splits the input string into a list of strings based on the separator. 

    The function uses two helper functions: 
        get_separator_indices() 
    and 
        split_words(). 
    """
    
    def get_separator_indices():
        c = 0
        separator_index = []
        for letter in range(len(my_str)):
            if my_str[letter] == separator:
                separator_index.append(letter)
                c = c + 1
    
        return separator_index, c

    [separator_indices, separator_number] = get_separator_indices()

    if separator_number == 0:
        output = my_str

    else:
        def split_words(separator_indices, c):

            my_list = []
            for k in range(c):
                if k != 0:
                    my_list.append(my_str[separator_indices[k-1] + 1:separator_indices[k]])
                elif k == 0:
                    my_list.append(my_str[0:separator_indices[k]]) 

            my_list.append(my_str[separator_indices[c-1] + 1:len(my_str)])            

            return my_list        

        output = split_words(separator_indices, separator_number)
    return output

# list = split_text(str,"|")
# print(list)
    

