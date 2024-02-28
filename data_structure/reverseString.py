from LinkedStack import LinkedStack

def reverse(string):
    stack = LinkedStack()
    for i in string:
        stack.push(i)
    reverse_str = ''
    for i in range(len(string)):
        reverse_str += stack.pop()
    return reverse_str

print(reverse('asd'))