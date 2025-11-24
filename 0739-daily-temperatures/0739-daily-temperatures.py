class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        sol = [0]*len(temperatures)
        st.append((temperatures[0],0))
        for i in range(len(temperatures)):
            prev = st[-1][0 ] if st else 0
            if temperatures[i] > prev and prev != 0:
                while st and st[-1][0]<temperatures[i]:
                    temp,ind = st.pop()
                    sol[ind] = i - ind
                st.append((temperatures[i],i))
            else:
                st.append((temperatures[i],i))
        return sol