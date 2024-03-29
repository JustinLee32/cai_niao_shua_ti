# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
# 示例 1：
#
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例 2：
#
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 示例 3：
#
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
#
# 说明：
#
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
#
# 进阶：
#
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        new_s = ""
        flag = 0
        for i in range(len(s)):
            if flag == 0:
                new_s += s[i]
                if not s[i].isspace():
                    pass
                else:
                    flag += 1
            elif flag == 1:
                if not s[i].isspace():
                    flag = 0
                    new_s += s[i]
                else:
                    continue
        words_list = new_s.split(" ")
        words_list.reverse()
        return " ".join(words_list)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords(" a good   example!   "))
