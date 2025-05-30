from game.Board import Board
from typing import Tuple, Optional


class Step:
    """
    Class that represents steps in the game and validation logic for the steps
    """
    CRAWL = 1
    JUMP = 2
    END = 3

    @staticmethod
    def _validate_end(src: Tuple[int, int], dest: Tuple[int, int]) -> bool:
        """
        Validate if the src and dest coordinates are the same for an END type of movement
        :param src: coordinate tuple of source peg
        :param dest: coordinate tuple of destination peg
        :return: validation boolean result
        """
        if src == dest:
            return True
        return False

    @staticmethod
    def _validate_crawl(board: Board, src: Tuple[int, int], dest: Tuple[int, int]) -> bool:
        """
        Validate if the src and dest coordinates are adjacent for a CRAWL type of movement
        :param board: board object
        :param src: source peg coordinate tuple
        :param dest: destination peg coordinate tuple
        :return: flag indicating if the movement is valid
        """
        x1, y1 = src
        x2, y2 = dest
        delta_x12 = abs(x1 - x2)
        delta_y12 = abs(y1 - y2)
        if (((delta_x12 == 1 and delta_y12 == 0) or
             (delta_x12 == 0 and delta_y12 == 1) or
             abs(x1 + y1 - (x2 + y2)) == 2 and delta_x12 == 1)
                and board.matrix[x2][y2] == 0):
            return True
        return False

    """
    @staticmethod
    def _validate_jump(board: Board, src: Tuple[int, int], dest: Tuple[int, int]) -> bool:
        
        Validate if the src and dest coordinates are valid for a JUMP type of movement - 6 permitted directions
        :param board: board object
        :param src: source peg coordinate tuple
        :param dest: destination peg coordinate tuple
        :return: flag indicating if the movement is valid
        
        x1, y1 = src
        x2, y2 = dest
        delta_x = abs(x1 - x2)
        delta_y = abs(y1 - y2)
        # Check valid jump pattern and empty destination
        if ((delta_x == 2 and delta_y == 0) or
            (delta_x == 0 and delta_y == 2) or
            (delta_x == 2 and delta_y == 2)):
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            # Can jump over any opponent's piece (not empty and not current player)
            if (board.matrix[mid_x][mid_y] != 0 and 
                board.matrix[mid_x][mid_y] != board.matrix[x1][y1] and
                board.matrix[x2][y2] == 0):
                return True
        return False
        """
       

    @staticmethod
    def validate_head(board: Board, src: Tuple[int, int], dest: Tuple[int, int]) -> Optional[int]:
        """
        Validate the movement after a change turn - CRAWL or JUMP - for the head of the move
        :param board: board object
        :param src: source peg coordinate tuple
        :param dest: destination peg coordinate tuple
        :return: flag indicating the type of movement allowed
        """
        if (abs(src[0] - dest[0]) <= 1 and abs(src[1] - dest[1]) <= 1
                and Step._validate_crawl(board, src, dest)):
            return Step.CRAWL
        #elif Step._validate_jump(board, src, dest):
        #    return Step.JUMP
        else:
            return None

    @staticmethod
    def validate_tail(board: Board, src: Tuple[int, int], dest: Tuple[int, int]) -> Optional[int]:
        """
        Validate the movement after a JUMP - JUMP or END - for the tail of the move
        :param board: board object
        :param src: source peg coordinate tuple
        :param dest: destination peg coordinate tuple
        :return: flag indicating the type of movement allowed
        """
        if Step._validate_end(src, dest):
            return Step.END
        #elif Step._validate_jump(board, src, dest):
        #    return Step.JUMP
        return None
