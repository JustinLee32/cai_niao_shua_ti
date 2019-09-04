# -*- coding: UTF-8 -*-
# Edit on July 20th, 2019

# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7

class Solution:
    # def countPrimes(self, n: int) -> int:
        # if n <= 2:
        #     return 0
        # temp_list = [i for i in range(2, n)]
        # temp_num = 0
        # while True:
        #     filter_number = temp_list[temp_num]
        #     temp_num += 1
        #     if filter_number ** 2 <= temp_list[-1]:
        #         temp_list = list(filter(lambda x: x % filter_number or x == filter_number, temp_list))
        #         # pass
        #     else:
        #         return len(temp_list)
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0     
        else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0],output[1] = 0,0
             # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
             # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2,int(n**0.5)+1): 
                if output[i] == 1:
                    output[i*i:n:i] = [0] * len(output[i*i:n:i])  # 以i=3为例，由于要找不能被2整除的3的倍数，故应该从i*i项开始查找
         # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
        return sum(output)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(11111111))
