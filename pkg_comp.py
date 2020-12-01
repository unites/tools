import os
import re

# This script/program is used to compare package lists pulled from Cerner's Environment Manager plan.
# It is basically just a real simple list comparison tool.
# Presumes file are in same directory as script, fill in filenames below
new_file = "new.dat"
old_file = "old.dat"

def _file_to_array(fname): 
    path = os.getcwd()
    result = []
    
    if fname:
        f_path = path + "/" + fname
    else:
        print("Invalid or No Filename Given.")
        exit()
    
    with open(f_path, 'r') as file:
        reader = file.readlines()
        for row in reader:
            pkg = []            
            pkg.append(re.sub(r'\,.*$','',re.sub(r'[^,]*$','',row.strip()))) # delete everything after first ,
            pkg.append(re.sub(r'^,\ ','',re.sub(r'^[^,]*','',row.strip()))) # delete everything before first ,
            result.append(pkg)

    return result

def get_diff(list1, list2):
    return (list(list(set(list1)-set(list2)) + list(set(list2)-set(list1))))

def compare():
    list1 = _file_to_array(new_file)
    list2 = _file_to_array(old_file)
    li1 = []
    li2 = []
    result = []


    for line in list1:
        li1.append(line[0])
    for line in list2:
        li2.append(line[0])
    pkg_diff = get_diff(li1, li2)

    for line in list2:
        list1.append(line)

    for line in list1:
        for row in pkg_diff:
            if line[0] in row:
                result.append(line)


    [print(line) for line in result]

compare()