class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:
            while st and k > 0 and st[-1] > int(digit):
                st.pop()
                k -= 1
            st.append(int(digit))
        while k > 0:
            st.pop()
            k -= 1
        result = ''.join(map(str, st)).lstrip('0')
        return result if result else "0"