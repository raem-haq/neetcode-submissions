# take n = 2 
#["()()","(())"]
#

def solve(n, st, m, s):
    if n == 0:
        s += ')'*m
        st.append(s)
    else:
        solve(n-1, st, m+1, s+'(')
        if m > 0:
            solve(n, st, m-1,s+')')


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        solve(n, st, 0, "")
        return st
