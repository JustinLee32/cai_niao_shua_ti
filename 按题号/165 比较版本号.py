# 比较两个版本号 version1 和 version2。
# 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
#
# 你可以假设版本字符串非空，并且只包含数字和 . 字符。
#
#  . 字符不代表小数点，而是用于分隔数字序列。
#
# 例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
#
# 你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
#  
#
# 示例 1:
#
# 输入: version1 = "0.1", version2 = "1.1"
# 输出: -1
# 示例 2:
#
# 输入: version1 = "1.0.1", version2 = "1"
# 输出: 1
# 示例 3:
#
# 输入: version1 = "7.5.2.4", version2 = "7.5.3"
# 输出: -1
# 示例 4：
#
# 输入：version1 = "1.01", version2 = "1.001"
# 输出：0
# 解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
# 示例 5：
#
# 输入：version1 = "1.0", version2 = "1.0.0"
# 输出：0
# 解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
#  
#
# 提示：
#
# 版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
# 版本字符串不以点开始或结束，并且其中不会有两个连续的点。
#


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        v1_list = list(map(int, v1_list))
        v2_list = list(map(int, v2_list))
        index = 0
        short = min(len(v1_list), len(v2_list))
        for i in range(short):
            if v1_list[i] > v2_list[i]:
                return 1
            elif v1_list[i] < v2_list[i]:
                return -1
            else:
                continue
        if len(v1_list) == len(v2_list):
            return 0
        elif len(v1_list) > len(v2_list):
            return 1 if sum(v1_list[len(v2_list):]) > 0 else 0
        else:
            return -1 if sum(v2_list[len(v1_list):]) > 0 else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion("1", "1.1"))
