# Python-Input output

To open a file, you can use the open() function in Python. It takes the file path and the mode as parameters and returns a file object. Here's an example:

file = open("filename.txt", mode="r")

To write text to a file, you can use the write() method of the file object. Here's an example:

file.write("Hello, world!")

To read the full content of a file, you can use the read() method of the file object. Here's an example:

content = file.read()

To read a file line by line, you can use a loop or the readline() method of the file object. Here's an example using a loop:

for line in file:
    print(line)

To move the cursor in a file, you can use the seek() method of the file object. It takes the offset and the optional whence parameter. Here's an example:

file.seek(0)  # Move the cursor to the beginning of the file

To make sure a file is closed after using it, you can call the close() method of the file object. However, a better practice is to use the with statement, which automatically takes care of closing the file. Here's an example:

with open("filename.txt", mode="r") as file:
    content = file.read()
    # Do something with the content
# File is automatically closed outside the `with` block

JSON (JavaScript Object Notation) is a popular data interchange format. It is commonly used to transmit data between a server and a web application, as it provides a human-readable and compact representation of data.

Serialization is the process of converting a data structure into a format that can be stored or transmitted, such as JSON. It allows you to save the state of an object or data structure.

Deserialization is the reverse process of serialization, where the serialized data is converted back into a data structure.

To convert a Python data structure to a JSON string, you can use the json.dumps() function. Here's an example:

import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
To convert a JSON string to a Python data structure, you can use the json.loads() function. Here's an example:

import json

json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
