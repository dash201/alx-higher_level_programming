#!/usr/bin/python3
if __name__ == "__main__":

    def new_in_list(my_list, idx, element):
        size = len(my_list)
        new_list = []
        if idx < 0:
            return (None)
        elif idx > size:
            return (None)
        else:
            for i in range(0, size):
                if i == idx:
                    new_list.append(element)
                else:
                    new_list.append(my_list[i])
            return (new_list)