package handler

import (
	"encoding/json"

	"github.com/ykn18/sudo-ku/board/model"
)

type SudokuBoard struct {
	board        [9][9]int
	solution     [9][9]int
	editableMask [9][9]bool
	blanks       int
}

type SudokuBoardJSON struct {
	model.SudokuBoard
}

func (s SudokuBoard) GetBoard() [9][9]int {
	return s.board
}

func (s *SudokuBoard) UnmarshalJSON(b []byte) error {
	temp := &SudokuBoardJSON{}

	if err := json.Unmarshal(b, &temp); err != nil {
		return err
	}

	s.board = temp.Board
	s.solution = temp.Solution
	s.blanks = 0
	for i, v := range s.board {
		for j, _ := range v {
			if s.board[i][j] == 0 {
				s.editableMask[i][j] = true
				s.blanks++
			}
		}
	}
	return nil
}
func (s SudokuBoard) CheckSolution(board [9][9]int) bool {
	return board == s.solution
}

func (s *SudokuBoard) Move(r, c, val int) (bool, int) {
	//Check if the position (r, c) is editable
	if s.editableMask[r][c] == true {
		if s.board[r][c] == 0 && val != 0 {
			s.blanks--
		}
		if s.board[r][c] != 0 && val == 0 {
			s.blanks++
		}
		s.board[r][c] = val
		return true, s.blanks
	}
	return false, s.blanks
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
	if b[r][c] == n {
		return true
	}
	return !isInRow(b, r, n) && !isInCol(b, c, n) && !isInSquare(b, r, c, n)
}
