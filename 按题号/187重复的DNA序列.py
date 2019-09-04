# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
#
# 示例:
#
# 输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s):
        dic = {}
        left = 0
        right = 10
        ans = []
        if len(s) <= 10:
            return ans
        while right <= len(s):
            if s[left:right] in dic:
                if dic[s[left:right]] == 1:
                    ans.append(s[left:right])
                    dic[s[left:right]] += 1
                left += 1
                right += 1
            else:
                dic[s[left:right]] = 1
                left += 1
                right += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
