class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ctr1,ctr2,ctr3 = 0,0,0
        for i in range(len(bills)):
            if bills[i] == 5:
                ctr1 += 1
                continue
            elif bills[i] == 10:
                if ctr1 >= 1:
                    ctr1 -= 1
                    ctr2 += 1
                else:
                    return False
            else:
                if ctr1 >= 1 and ctr2 >= 1:
                    ctr1 -= 1
                    ctr2 -= 1
                    ctr3 += 1
                    continue
                if ctr1 >= 3:
                    ctr1 -= 3
                    ctr3 += 1
                    continue
                else:
                    print("failed at - "+str(i)+" where bills[i] is "+str(bills[i])+" where ctr1 = "+str(ctr1)+", ctr2 = "+str(ctr2)+" ,ctr3 = "+str(ctr3))
                    return False
        return True