from typing  import *

# WA 这个忽略掉了 RRS的情况 RRS的话碰撞是2次 但我的代码是1次
class Solution:
    def countCollisions(self, directions: str) -> int:
        from collections import deque
        ans = 0
        q = deque(directions)
        while len(q) > 1:
            a, b = q.popleft(), q.popleft() 
            if a == "R" and b == "L":
                ans += 2
                q.appendleft("S")
            elif a == "R" and b == "S":
                ans += 1
                q.appendleft("S")
                q.appendleft("S")
            else:
                q.appendleft(b)
        return ans


class Solution1:
    def countCollisions(self, directions: str) -> int:
        from collections import deque
        ans, save = 0, 0 # save用来指示一个R前面有多少个紧邻的R
        q = deque(directions)
        while len(q) > 1:
            a, b = q.popleft(), q.popleft() 
            if a == "R" and b == "L":
                ans += 2 + save # 当R发生碰撞就会变成S，前面紧邻的所有R都会依次发生碰撞
                q.appendleft("S")
                save = 0
            elif a == "R" and b == "S":
                ans += 1 + save
                q.appendleft("S")
                save = 0
            elif a == "S" and b == "L":
                ans += 1
                q.appendleft("S")
            elif a == "R" and b == "R":
                save += 1
                q.appendleft("R")
            else:
                q.appendleft(b)
        return ans



def main():
    sol = Solution1()
    _input = ("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR", )
    _output = sol.countCollisions(*_input)
    print(_output)

if __name__ == '__main__':
    main()
