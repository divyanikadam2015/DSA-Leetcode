class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}

        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word
        
        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            ch = board[i][j]

            if ch not in node:
                return

            node = node[ch]

            if '#' in node:
                res.append(node.pop('#'))

            board[i][j] = '*'

            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != '*':
                    dfs(x, y, node)

            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res       
        