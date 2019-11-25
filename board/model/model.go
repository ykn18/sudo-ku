package model

type SudokuBoard struct {
	Board    [9][9]int
	Solution [9][9]int
	Blanks   int
}
