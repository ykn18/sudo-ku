package handler

import (
	"sudo-ku/board/model"
)

type SudokuBoard model.SudokuBoard

func (s SudokuBoard) CheckSolution() bool {
	return s.Board == s.Filled
}

func (s SudokuBoard) Move(r, c, val int) bool {
	if isLegal(s.Board, r, c, val) {
		s.Board[r][c] = val
		return true
	} else {
		return false
	}
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
