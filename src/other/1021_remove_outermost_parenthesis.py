def removeOuterParentheses(S):
    stack = []
    primitive = ''
    prim_list = []

    for i in S:
        primitive += i
        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()
            if len(stack) == 0:
                prim_list.append(primitive)
                primitive = ''

    for i in range(len(prim_list)):
        prim_list[i] = prim_list[i][1:len(prim_list[i]) - 1]

    return ''.join(prim_list)


if __name__ == "__main__":
    # a = '(()())(())'
    # a = '(()())(())(()(()))'
    a = '()()'
    x = removeOuterParentheses(a)
    print(x)
