def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # created result array & directory dictionary
    result = []
    directory = dict()

    # loop through files to get each files
    for file in files:
        # split the file with "/"
        split_section = file.split("/")

        # then take the last item from the file
        filename = split_section[-1]

        # if the file name is not in the directory we will create it with [] to include directory location.
        if filename not in directory:
            directory[filename] = []

        # then we add the filename to the directory dictionary.
        directory[filename].append(file)

    # print(directory)

    # find query filename within the queries
    for query in queries:
        # if query filename match the directory
        if query in directory:
            # then we add the query to the result.
            result.extend(directory[query])

    return result


if __name__ == "__main__":
    test_files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    test_query = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(test_files, test_query))
