/*
Runtime:            262 ms
Beats:              31.43%
Memory:             2.34 MB
Beats:              17.72%
Submission:         https://leetcode.com/problems/word-search/submissions/1478708538/
Time complexity:    O(n^3)
Space complexity:   O(n^2)
Topics:             #backtracking, #bfs, #dfs
Solved By:          #dfs
*/

struct Solution {}

impl Solution {
    fn dfs(
        row: usize,
        col: usize,
        index: usize,
        board: &[Vec<char>],
        visited: &mut Vec<Vec<bool>>,
        word: &str,
    ) -> bool {
        if index == word.len() {
            return true;
        }
        if row >= board.len()
            || col >= board[0].len()
            || visited[row][col]
            || board[row][col] != word.chars().nth(index).unwrap()
        {
            return false;
        }

        visited[row][col] = true;

        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        for (r, c) in directions {
            let new_row = (row as i32 + r) as usize;
            let new_col = (col as i32 + c) as usize;
            if Self::dfs(new_row, new_col, index + 1, board, visited, word) {
                return true;
            }
        }

        visited[row][col] = false;
        false
    }

    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let rows = board.len();
        let cols = board.get(0).unwrap().len();

        for row in 0..rows {
            for col in 0..cols {
                if board[row][col] == word.chars().nth(0).unwrap()
                    && Self::dfs(
                        row,
                        col,
                        0,
                        &board,
                        &mut vec![vec![false; cols]; rows],
                        &word,
                    )
                {
                    return true;
                }
            }
        }

        false
    }
}

fn main() {
    let board = Vec::from([
        Vec::from(['A', 'B', 'C', 'E']),
        Vec::from(['S', 'F', 'C', 'S']),
        Vec::from(['A', 'D', 'E', 'E']),
    ]);
    let word = "ABCCED".to_string();

    let result = Solution::exist(board, word);
    println!("{}", result);
}
