class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w

        rows, cols = len(board), len(board[0])
        res = set()

        def dfs(r, c, node):
            char = board[r][c]
            curr_node = node.children[char]

            # Check if we found a word
            if curr_node.word:
                res.add(curr_node.word)
                # Optimization: remove word to avoid duplicates
                # curr_node.word = None 

            # Temporarily mark the cell as visited
            board[r][c] = '#'

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Restore the cell
            board[r][c] = char

            # Optimization: Prune leaf nodes to speed up future searches
            if not curr_node.children:
                del node.children[char]

        # Step 2: Backtracking from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return list(res)