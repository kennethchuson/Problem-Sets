

'''

s = "abcdef"
arr = ['ab', 'abc', 'cd', 'def', 'abcd']




'''


def solve(target, wordbank):

    if target == '':
        return True

    for word in wordbank:
        if target.startswith(word):
            suffix = target.replace(word, '', 1)
            if solve(suffix, wordbank) == True:
                return True

    return False

s = 'aabbc'
arr = ['aa','b','c']

out = solve(s, arr) 

print(out) 
