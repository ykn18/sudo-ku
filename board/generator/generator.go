package generator

import (
	"math/rand"
	"sudo-ku/board/model"
	"time"
)

type SudokuBoard struct {
	model.SudokuBoard
}

func MakeSudokuBoard(difficulty string) model.SudokuBoard {
	b, sol, count := makeBoardAndSolution(difficulty)
	return model.SudokuBoard{Board: b, Solution: sol, Blanks: count}
}

func makeFilledBoard(board [9][9]int, rowStart, colStart int) ([9][9]int, bool) {
	done := false

	if colStart == 9 {
		colStart = 0
		rowStart++
		if rowStart == 9 {
			return board, true
		}
	}

	guesses := [9]int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	rand.Shuffle(9, func(a, b int) {
		guesses[b], guesses[a] = guesses[a], guesses[b]
	})

	for _, guess := range guesses {
		if isLegal(board, rowStart, colStart, guess) {
			board[rowStart][colStart] = guess
			board, done = makeFilledBoard(board, rowStart, colStart+1)
		}
		if done {
			return board, done
		}
	}

	board[rowStart][colStart] = 0
	return board, done
}

func countSolutions(board [9][9]int, rowStart, colStart int) int {
	count := 0
	branchCount := 0

	if colStart == 9 {
		colStart = 0
		rowStart++
		if rowStart == 9 {
			return 1
		}
	}

	if board[rowStart][colStart] != 0 {
		return countSolutions(board, rowStart, colStart+1)
	}

	for guess := 1; guess < 10 && count < 2; guess++ {
		if isLegal(board, rowStart, colStart, guess) {
			board[rowStart][colStart] = guess
			branchCount = countSolutions(board, rowStart, colStart+1)
			count = count + branchCount
		}
	}

	board[rowStart][colStart] = 0
	return count
}

func makeEmptyBoard() [9][9]int {
	emptyBoard := [9][9]int{
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
	}
	return emptyBoard
}

func makeBoardAndSolution(difficulty string) ([9][9]int, [9][9]int, int) {
	rand.Seed(time.Now().UTC().UnixNano())
	emptyBoard := makeEmptyBoard()

	var goal int
	switch difficulty {
	case "easy":
		goal = 32
	case "medium":
		goal = 28
	case "hard":
		goal = 24
	}

	filledBoard, _ := makeFilledBoard(emptyBoard, 0, 0)
	generatedBoard := filledBoard
	var positions [81]int
	for i := 0; i < 81; i++ {
		positions[i] = i
	}
	rand.Shuffle(81, func(a, b int) {
		positions[b], positions[a] = positions[a], positions[b]
	})
	var guess, row, col int
	remaining := 81
	for _, p := range positions {
		row, col = p/9, p%9
		guess = generatedBoard[row][col]
		generatedBoard[row][col] = 0
		if countSolutions(generatedBoard, 0, 0) > 1 {
			generatedBoard[row][col] = guess
		} else {
			remaining -= 1
		}
		if remaining == goal {
			return generatedBoard, filledBoard, 81 - goal
		}
	}
	return generatedBoard, filledBoard, 81 - goal
}

func isInRow(b [9][9]int, r, n int) bool {
	for i := 0; i < 9; i++ {
		if b[r][i] == n {
			return true
		}
	}
	return false
}

func isInCol(b [9][9]int, c, n int) bool {
	for i := 0; i < 9; i++ {
		if b[i][c] == n {
			return true
		}
	}
	return false
}

func isInSquare(b [9][9]int, r, c, n int) bool {
	rowStart := r - r%3
	colStart := c - c%3
	for i := rowStart; i < (rowStart + 3); i++ {
		for j := colStart; j < (colStart + 3); j++ {
			if b[i][j] == n {
				return true
			}
		}
	}
	return false
}

func isLegal(b [9][9]int, r, c, n int) bool {
	return !isInRow(b, r, n) && !isInCol(b, c, n) && !isInSquare(b, r, c, n)
}
