from stack import stack
def is_match(p1,p2):
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '{' and p2 == '}':
        return True
    return False
def is_balanced(paren_str):
    s = stack()
    is_balanced = True
    i = 0
    while i < len(paren_str) and is_balanced:
        paren = paren_str[i]
        if paren in'{[(':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        i=i+1
    if s.is_empty() and is_balanced:
        return True
    return False


print(is_balanced('}{'))

