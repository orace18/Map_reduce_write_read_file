import os
def map(key,value):
    intermediate = []
    for word in value.split():
        intermediate.append((word,1))
    return intermediate

def reduce(key,value):
    result = 0
    for c in value:
        result = result + c
    return (key, result)

def shuffle_sort(tabs):
    out = []
    for tab_of_map in tabs:
        for data in tab_of_map:
            present = False
            for o in out:
                if o[0] is data[0]:
                    o[1].append(data[1])
                    present = True
                    break

            if present is False:
                out.append((data[0],[data[1]]))

    return out

def read_files(directory):
    files = []
    for file in os.listdir(directory):

        files.append(directory + '/' + file)
    return files

if __name__ == "__name":

    directory = "C:/xampp"
    files = read_files(directory)
    map_input = []
    map_output = []
    for file in files:
        with open(file, 'r') as f:
            map_input.append(f.read().replace(".", "").replace(",",""))

    for i in range(len(map_input)):
        map_output.apprend(map(str(i),map_input[i]))

    result = shuffle_sort(map_input)
    reduce_output = []
    for data in result:
        reduce_output.append(reduce(data[0], data[1]))

    for r in reduce_output:
        print(r)
