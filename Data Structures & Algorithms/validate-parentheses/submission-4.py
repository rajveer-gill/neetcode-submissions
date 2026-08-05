class Solution:
    def isValid(self, s: str) -> bool:
        left = {'{', '[', '('}
        right = {'}', ']', ')'}
        queue = []

        for x in s:
            if x in left:
                queue.append(x)
            if x in right:
                if len(queue) == 0:
                    return False
                else:
                    if queue[len(queue) - 1] == '[' and x == ']':
                        queue.pop()
                    elif queue[len(queue) - 1] == '{' and x == '}':
                        queue.pop()
                    elif queue[len(queue) - 1] == '(' and x == ')':
                        queue.pop()
                    else:
                        return False
        

        if len(queue) > 0:
            return False
        return True



        