import itertools
def reverseParentheses(s):
    if s.count('(') == 0 and s.count(')') == 0:
        return s
    rev_s = stringInParentheses(s)
    s = s[:s.index(rev_s) - 1] + rev_s[::-1] + s[s.index(rev_s) + len(rev_s) + 1:]
    return reverseParentheses(s)

def stringInParentheses(s):
    last_bracket = s.rindex('(')
    return ''.join(list(itertools.takewhile(lambda x: x != ')', s[last_bracket + 1:])))