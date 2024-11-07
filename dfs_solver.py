# dfs_solver.py
from state import PuzzleState
from n_puzzle import generate_goal_state, generate_random_start_state

def depth_first_search(start_state, goal_state):
    """
    Hàm triển khai thuật toán Depth First Search (DFS) để tìm lời giải.
    - start_state: Trạng thái khởi đầu của bài toán.
    - goal_state: Trạng thái đích cần đạt được.
    - Trả về danh sách các bước di chuyển từ trạng thái khởi đầu đến đích, hoặc None nếu không có giải pháp.
    """
    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        
        if current_state.is_goal(goal_state.matrix):
            return path  # Trả về danh sách các bước nếu tìm thấy lời giải

        visited.add(current_state)

        for move in current_state.possible_moves():
            if move not in visited:
                stack.append((move, path + [move]))

    return None  # Không tìm thấy giải pháp

if __name__ == "__main__":
    k = 3  # Kích thước ma trận, ví dụ: 3 cho bài toán 8-puzzle
    start_state = generate_random_start_state(k)
    goal_state = generate_goal_state(k)

    print("Trạng thái ban đầu:")
    print(start_state)
    print("\nTrạng thái mục tiêu:")
    print(goal_state)
    print("\nĐang tìm kiếm lời giải...\n")

    solution = depth_first_search(start_state, goal_state)

    if solution:
        print("Đã tìm thấy giải pháp!")
        for step, state in enumerate(solution):
            print(f"Step {step}:\n{state}\n")
        print("Trạng thái cuối cùng đạt được trạng thái đích.")
    else:
        print("Không tìm thấy giải pháp.")
