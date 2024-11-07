# n_puzzle.py
import random
from state import PuzzleState

def generate_goal_state(k):
    """
    Tạo trạng thái kết thúc cho trò chơi N-puzzle.
    
    Parameters:
    k (int): Kích thước của ma trận (k x k).
    
    Returns:
    PuzzleState(goal_matrix, (k-1, k-1)): tạo một đối tượng PuzzleState 
    với ma trận goal_matrix và vị trí của ô trống ở góc dưới bên phải (k-1, k-1).
    """

    # Tạo ma trận k x k chứa giá trị từ 1 tới N(k*k-1) theo thứ tự và ô trống (số 0) nằm ở vị trí cuối cùng
    goal_matrix = [[(i * k + j + 1) % (k * k) for j in range(k)] for i in range(k)]
    return PuzzleState(goal_matrix, (k-1, k-1))

def generate_random_start_state(k):
    """
    Tạo trạng thái khởi đầu ngẫu nhiên cho trò chơi N-puzzle.
    
    Parameters:
    k (int): Kích thước của ma trận (k x k).
    
    Returns:
    PuzzleState(matrix, empty_tile) tạo một đối tượng PuzzleState 
    với ma trận matrix ngẫu nhiên và vị trí của ô trống (empty_tile).
    """

    # Tạo danh sách chứa các số từ 1 đến k*k-1 và số 0 (ô trống)
    matrix = list(range(1, k * k)) + [0]
    # Xáo trộn danh sách để tạo trạng thái ngẫu nhiên
    random.shuffle(matrix)
    # Chuyển danh sách thành ma trận k x k
    matrix = [matrix[i * k:(i + 1) * k] for i in range(k)]
    # Xác định vị trí của ô trống (số 0)
    empty_tile = [(i, row.index(0)) for i, row in enumerate(matrix) if 0 in row][0]
    return PuzzleState(matrix, empty_tile)
