def ladderLength(beginWord, endWord, wordList):
    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """

            if endWord not in wordList:
                return 0

            wordList = set(wordList)
            head = [beginWord]
            tail = [endWord]
            count = 2
            while (head and tail):
                tmpList = []
                if len(head) > len(tail):
                    head, tail = tail, head
                for word in head:
                    for i in range(len(word)):

                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            tmp = word[:i] + j + word[i + 1:]
                            if tmp in tail:
                                return count
                            if tmp in wordList:
                                tmpList.append(tmp)
                                wordList.remove(tmp)
                count += 1
                head = tmpList
            return 0
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
t = ladderLength(beginWord,endWord,wordList)
print(t)