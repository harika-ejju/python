from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Step 1: Build the graph using BFS (find the shortest path)
        layer = {}
        layer[beginWord] = [[beginWord]]  # Dict[word] = list of paths reaching this word
        
        while layer:
            next_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]  # Return all paths that reached the endWord
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            for path in layer[word]:
                                next_layer[new_word].append(path + [new_word])
            # Remove visited words to prevent cycles
            wordSet -= set(next_layer.keys())
            layer = next_layer
        
        return []

# 🧪 Example Test
sol = Solution()
begin = "hit"
end = "cog"
dictionary = ["hot","dot","dog","lot","log","cog"]
results = sol.findLadders(begin, end, dictionary)

print("All shortest transformation sequences:")
for path in results:
    print(path)
