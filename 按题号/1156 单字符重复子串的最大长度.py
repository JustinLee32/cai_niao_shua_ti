class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import defaultdict
        if len(text) == 1:
            return 1
        words_count_dict = defaultdict(int)
        ans = 0
        for i in range(len(text)):
            words_count_dict[text[i]] += 1
        cache, record = "", ""
        slow, fast, flag, temp_count = 0, 0, 0, 0
        while fast <= len(text) - 1:
            if not cache:
                record = text[fast]
                cache += text[fast]
                temp_count += 1
                fast += 1
            else:
                if not flag:
                    cache += text[fast]
                    if text[fast] != record:
                        flag += 1
                        slow = fast
                    else:
                        temp_count += 1
                    fast += 1
                elif flag == 1:
                    if text[fast] != record:
                        if temp_count < words_count_dict[record]:
                            ans = max(ans, temp_count + 1)
                        else:
                            ans = max(ans, temp_count)
                        temp_count = 0
                        fast = slow
                        cache = ""
                        flag = 0
                    else:
                        cache += text[fast]
                        temp_count += 1
                        fast += 1
        if cache:
            if temp_count < words_count_dict[record]:
                ans = max(ans, temp_count + 1)
            else:
                ans = max(ans, temp_count)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxRepOpt1(text="bbababaaaa"))
