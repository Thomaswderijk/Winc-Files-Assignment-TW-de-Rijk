__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

"""First, the imports
"""

import os
import zipfile

"""Defining the clean_cache function:
The function checks if "cache" exists
If so, it for-loops through the files in "chache"
and deletes them.
Else it makes a "cache" directory
"""


def clean_cache():
    if "cache" in os.listdir(os.path.join(os.getcwd(), "files")):
        for files in os.listdir(os.path.join(os.getcwd(), "files", "cache")):
            os.remove(os.path.join(os.getcwd(), "files", "cache", files))
    else:
        os.mkdir(os.path.join(os.getcwd(), "files", "cache"))


"""Defining the cache_zip function:
First the function runs clean_cache
to get the clean 'cache' directory.
Then we make the file_path into a zipfile object
so we can extract all the contents to dir_path.
"""


def cache_zip(file_path, dir_path):
    clean_cache()
    zip_path = zipfile.ZipFile(file_path)
    zip_path.extractall(dir_path)


"""Defining the cached_files function:
This function will walk through
the 'cache' directory and only return
the filepaths in a list.
Then it loops through that list to
get the absolute filepaths and add them
to the final list.
"""


def cached_files():
    file_path_list = []
    for folders, subfolders, files in os.walk(
        # folders/subfolders aren't used but ensure that no dir are in the list
        os.path.join(os.getcwd(), "files", "cache")
    ):

        for file in files:
            file_path_list.append(
                os.path.join(os.getcwd(), "files", "cache", str(file))
            )
    return file_path_list


"""Defining the find_password function:
This function for-loops through the file_paths,
opens every file and converts it to a readable string.
If the term 'password' is found
it wil split the string and index the word after 'password'
And will also close any opened files after use.
"""


def find_password(file_paths):
    for file in file_paths:
        open_file = open(file, "r")
        read_file = open_file.read()
        if read_file.find("password") != -1:
            password = read_file[read_file.find("password") :].split()[1]
            open_file.close()
        else:
            open_file.close()

    return password
