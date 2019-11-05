from typing import List
from collections import defaultdict


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_split = []
        ans = []
        for file in folder:
            folder_split.append(file.lstrip('/').split('/'))
        folder_split.sort(key=lambda x: len(x))
        cache_dict = defaultdict(set)
        for file in folder_split:
            flag = 1
            size = len(file)
            temp = ''.join(file)
            i = 0
            cache = ''
            while i < size - 1:
                cache += file[i]
                if cache in cache_dict[i+1]:
                    flag = 0
                    break
                i += 1
            if flag:
                cache_dict[size].add(temp)
                ans.append('/' + '/'.join(file))
        return ans


if __name__ == '__main__':
    folder = ["/ad", "/ad/af", "/aa"]
    sol = Solution()
    print(sol.removeSubfolders(folder))
