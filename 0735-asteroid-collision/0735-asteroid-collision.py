class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                st.append(asteroids[i])
            else:
                while len(st)>0 and st[-1]>0 and st[-1]<abs(asteroids[i]):
                    st.pop()
                if len(st)>0 and st[-1] == abs(asteroids[i]):
                    st.pop()
                elif(not st or st[-1]<0):
                    st.append(asteroids[i])
        return st