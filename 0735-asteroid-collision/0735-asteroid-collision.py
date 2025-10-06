class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                st.append(asteroids[i])
            else:
                destroyed = False
                while len(st)>0 and st[-1]>0 and st[-1]<=abs(asteroids[i]):
                    if st[-1] == abs(asteroids[i]):
                        destroyed = True
                        st.pop()
                        break
                    else:
                        st.pop()
                if len(st)>0 and st[-1] > abs(asteroids[i]):
                    continue
                print("currently on - "+str(asteroids[i]))
                if not destroyed:
                    st.append(asteroids[i])
        return st