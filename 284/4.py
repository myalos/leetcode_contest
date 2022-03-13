from typing  import *

# 所有算法里面我最喜欢图算法和动态规划
# 这是一个双源的问题，如果是单元 那么就用最短路就行了
# 如果有两个源一条路的最短路上面权重是100 是从A到B B到C是1 然后A到C是10，对于第二个源走到A的时候要到C 那么如果用最短路 走的就是A C 然而其实A B C耗费更少
# idea 有了 就是A走完最短路的时候 把A经过的路线权重都改成0
# 同时有个问题出现在脑海，有没有可能两个路都不是最短路

# 比如起点A 和B 终点C
# A -> D : 1 ; B -> D : 1; D -> E : 5; E -> C : 1;
# A -> G : 2 ; G -> H : 2; H -> C : 2;
# B -> J : 2 ; J -> K : 2; K -> C : 2;
# 如果两个都是最短路 那么花费是12 如果都不是那么就是1 5 1

# 假设它们公同走的路程为p -> ... -> q 那么q 是终点没毛病，如果q不是终点，那么q到终点 两个源走的不一样，那么一定有条最短的，另一条走这条最短的是更优解。
# 这题就分段 找p点 然后总距离就是两个源点到p的最短路加上p到终点的最短路

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # todo
        return 0

def main():
    sol = Solution()
    _input = (6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 0, 1, 5)
    _output = sol.minimumWeight(*_input)
    print(_output)

if __name__ == '__main__':
    main()
