# state.py
class PuzzleState:
    def __init__(self, matrix, empty_tile):
        """
        Khởi tạo trạng thái của bài toán.
        - matrix: Ma trận k x k đại diện cho trạng thái hiện tại của bài toán.
        - empty_tile: Vị trí của ô trống trong ma trận, dạng (row, col).
        """
        self.matrix = matrix  # Ma trận k x k
        self.empty_tile = empty_tile  # Vị trí của ô trống (dòng, cột)
        self.k = len(matrix)  # Kích thước của ma trận

    def move_tile(self, direction):
        """
        Di chuyển ô trống theo hướng chỉ định.
        - direction: Hướng di chuyển ('left', 'right', 'up', 'down').
        - Trả về trạng thái mới nếu di chuyển hợp lệ, hoặc None nếu không di chuyển được.
        """
        row, col = self.empty_tile
        if direction == "left" and col > 0:
            new_col = col - 1
            return self._swap_tiles(row, col, row, new_col)
        elif direction == "right" and col < self.k - 1:
            new_col = col + 1
            return self._swap_tiles(row, col, row, new_col)
        elif direction == "up" and row > 0:
            new_row = row - 1
            return self._swap_tiles(row, col, new_row, col)
        elif direction == "down" and row < self.k - 1:
            new_row = row + 1
            return self._swap_tiles(row, col, new_row, col)
        return None

    def _swap_tiles(self, row1, col1, row2, col2):
        """
        Hoán đổi ô trống với ô ở vị trí đích.
        - row1, col1: Vị trí hiện tại của ô trống.
        - row2, col2: Vị trí đích muốn di chuyển.
        - Trả về trạng thái mới sau khi di chuyển.
        """
        new_matrix = [row[:] for row in self.matrix]  # Sao chép ma trận hiện tại
        new_matrix[row1][col1], new_matrix[row2][col2] = new_matrix[row2][col2], new_matrix[row1][col1]
        return PuzzleState(new_matrix, (row2, col2))

    def is_goal(self, goal_matrix):
        """
        Kiểm tra xem trạng thái hiện tại có phải là trạng thái kết thúc không.
        - goal_matrix: Ma trận trạng thái đích cần so sánh.
        - Trả về True nếu đạt trạng thái đích, ngược lại False.
        """
        return self.matrix == goal_matrix

    def possible_moves(self):
        """
        Sinh các trạng thái hợp lệ từ trạng thái hiện tại bằng cách di chuyển ô trống.
        - Trả về danh sách các trạng thái mới có thể sinh ra.
        """
        moves = []
        for direction in ["left", "right", "up", "down"]:
            new_state = self.move_tile(direction)
            if new_state:
                moves.append(new_state)
        return moves

    def __eq__(self, other):
        """
        So sánh hai trạng thái dựa trên ma trận.
        - Trả về True nếu giống nhau, ngược lại False.
        """
        return self.matrix == other.matrix

    def __hash__(self):
        """
        Tạo mã băm cho trạng thái để sử dụng trong các cấu trúc dữ liệu tập hợp.
        """
        return hash(tuple(tuple(row) for row in self.matrix))

    def __str__(self):
        """
        Chuyển trạng thái thành chuỗi để dễ dàng hiển thị.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        """
        Đại diện chuỗi của đối tượng cho mục đích gỡ lỗi.
        """
        return self.__str__()
