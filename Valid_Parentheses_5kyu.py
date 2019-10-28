def valid_parentheses(string):
    open = 0
    close = 0
    parentheses = ""
    if len(string) == 0:
        return True
    for letter in string:
        if letter == "(":
            open += 1
            parentheses += letter
        elif letter == ")":
            close += 1
            parentheses += letter
        if close > open:
            return False
    if open == close and parentheses[0] == "(" and parentheses[-1] == ")":
        return True
    else:
        return False
