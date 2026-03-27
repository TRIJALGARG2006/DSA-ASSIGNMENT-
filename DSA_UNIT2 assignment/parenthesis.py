def checkParenthesis(expr):
    stk = []
    for ch in expr:
        if ch in "{[(":
            stk.append(ch)
        if ch in "}])":
            if not stk:
                return False
            top = stk[-1]
            match ch:
                case "}":
                    if top != "{":
                        return False
                    else:
                        stk.pop()
                case "]":
                    if top != "[":
                        return False
                    else:
                        stk.pop()
                case ")":
                    if top != "(":
                        return False
                    else:
                        stk.pop()
                        
    return True

def main():
    expr = "({[]})"
    print(checkParenthesis(expr))

if __name__ == "__main__":
    main()