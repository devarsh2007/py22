name = "python"
print(len(name))

# position - index
# start = 0
# end = lenth - 1
# [:] slice operator
# string_name[position]

# direct access
print(name[0])
print(name[5])
print(name[2])

number = "1234"
print(number[1])

# range access
# string_name[start_position : end_position+1]
name = "hello world "
print(name[0:5])
print(name[6:11])
print(name[4:7])
print(name[0:11])

text = """
    this is first line
    this is second line 
    this is third line
"""
last = len(text) - 1

print(text[0:last])