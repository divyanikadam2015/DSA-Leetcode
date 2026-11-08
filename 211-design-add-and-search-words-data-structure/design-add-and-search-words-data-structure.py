class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node

            if word[i] == '.':
                return any(dfs(node[ch], i + 1) for ch in node if ch != '#')

            if word[i] not in node:
                return False

            return dfs(node[word[i]], i + 1)

        return dfs(self.root, 0)