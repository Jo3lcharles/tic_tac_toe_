def separate_numbers(nested_list:list[list[int]]) -> dict[str,dict[str, list[int]]]:
    #make sure the input is a list
    assert isinstance(nested_list,list), "invalid argument"
    #ensure it has an inner loop and the inner loop contains intergers
    for list_ in nested_list:
        if not isinstance(list_, list):
            raise AssertionError("invalid argument")
        for element in list_:
            if not isinstance(element, int):
                raise AssertionError("invalid argument")
            
    outer_dict = {}   
    for i , inner_list in enumerate(nested_list):
        odd_list = [x for x in inner_list if x%2 != 0]
        even_list = [x for x in inner_list if x%2 == 0]
        inner_dict = {"list" : inner_list , "odd" : odd_list, "even" : even_list}
        outer_dict[f"list_number_{i}"] = inner_dict

    return outer_dict



from statistics import mean

def co_efficient(list_1: list[int], list_2:list[int]):
    avg_ref = mean(list_1)
    avg_list = mean(list_2)
    numerator = 0
    denominator1 = 0
    denominator2 = 0

    for a,b in zip(list_1 , list_2):
        difference1 = a - avg_ref
        difference2 = b - avg_list
        numerator+=(difference1 * difference2)
        denominator1 +=difference1**2
        denominator2 += difference2**2

    denominator = (denominator1 * denominator2)** 0.5

    if denominator == 0:
        raise AssertionError("denominator cant be 0")
    else:
        co_efficient = numerator/ denominator

    return co_efficient


def highest_col(ref:list[int], nested_list: list[list[int]]):
    compare = []
    for list_ in nested_list:
        if len(list_) != len(ref):
            raise AssertionError(" inner list must be of the same length as the reference list")
    for sublist in nested_list:
        co_efficient_ = co_efficient(ref, sublist)

        compare.append(co_efficient_)
    return (nested_list[compare.index(max(compare))] , round(max(compare), 4))



def initialize_board(n: int) -> list[list[str]]:
    return [[" "]*n for i in range(n)]
    for i in range(n):
        result.append([' '] *n)
    return result

# This function is provided, and you can leave it as is.
def print_board(board: list[list[str]]) -> None:
    """
    Print the current state of the game board.
    
    >>> print_board([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    >>> print_board([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])
    -------------
    |   | X |   |
    -------------
    |   |   |   |
    -------------
    |   |   | O |
    -------------
    """
    print('-' * (4 * len(board[0]) + 1))
    for row in board:
        print('|', end = '')
        for cell in row:
            print(f" {cell} |", end = "")
        print('\n' + '-' * (4 * len(row) + 1))

def drop_piece(board: list[list[str]], row: int, col: int, player: str) -> bool:
    """
    Allow a player to drop their piece into a specified cell on the board. You can only drop a piece to a cell that is unoccupied.

    Returns:
    - bool: True if the piece is successfully dropped, False if the cell is already occupied.
    """
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

def is_winner(board: list[list[str]], player: str) -> bool:
    """
    Check if a player has won the game. A player win the game if the pieces placed by the player are in row, columns or diagonals

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    n = len(board)
    #check the rows
    for row in board:
        if all(cell == player for cell in row):
            pass
        if row == ["X"] *len(row) or row == ["O"]* len(row):
            return True
        else:
            continue

    #check the columns
    for col in range(n):
        if all(board[row][col] == player for row in range(n) ):
            pass
        temp = []
        for row in range(n):
            temp.append(board[row][col])
        if temp == ["X"] *len(temp) or temp == ["O"]* len(temp):
            return True
        else:
            continue

    #check the diagonal
    if all(board[i][i] == player for i in range(n)):
        pass
    temp =[]
    for i in range(n):
        for j in range(n):
            if i == j:
                temp.append(board[i][j])
        if temp == ["X"] *n or temp == ["O"]* n:
            return True
        else:
            continue

    if all(board[i][n-i-1] == player for i in range(n)) :
        pass   
    temp =[]
    for i in range(n):
        for j in range(n):
            if i+j == n - 1:
                temp.append(board[i][j])
    if temp == ["X"] *n or temp == ["O"]* n:
        return True
    else:
        return False
        


def is_board_full(board: list[list[str]]) -> bool:

    """
    Check if the game board is full, indicating a tie if there is no winner.
    """
    return all(cell != " " for row in board for cell in row )
    flat_board = [j for i in board for j in i ]
    return "".join(flat_board).isalpha()

    for row in board:
        for col in row:
            if col == " ":
                return False
    return True   
    

# This function is provided, and you can leave it as is.
def play_tic_tac_toe() -> None:
    """ Orchestrate the game, allowing two players to take turns."""
    print("Welcome to Tic-Tac-Toe!")
    
    # Initialize the game board
    n = 0
    while n < 3:
        try:
            n = int(input("What is size of the board? ").strip())
        except:
            continue
            
    board = initialize_board(n)    

    # Define players
    players = ['X', 'O']
    current_player = 0
    
    player_1_name = input("What is the name of player 1? ").strip()
    player_2_name = input("What is the name of player 2? ").strip()
    if not player_1_name:
        player_1_name = '1'
    if not player_2_name:
        player_2_name = '2'
        
    player_names = [player_1_name, player_2_name]
    
    continue_game = True

    while continue_game:
        print_board(board)

        # Get player input
        # As we are facing regular players, the row and col start 1 so that they don't get confused
        row_col_examples = '/'.join([str(i + 1) for i in range(n)])
        row = input(f"Player {player_names[current_player]}, choose a row ({row_col_examples}): ").strip()
        col = input(f"Player {player_names[current_player]}, choose a column ({row_col_examples}): ").strip()
        
        try:
            row = int(row) - 1
            col = int(col) - 1
            item_range = ", ".join([str(i + 1) for i in range(n)])
            assert row in [i for i in range(n)] and col in [i for i in range(n)], f"row and col must be an int ranged from {item_range}"
        except:
            print("row and col must be an int ranged from 1, 2, 3")
            continue
        
        # Drop the player's piece into the chosen cell
        if drop_piece(board, row, col, players[current_player]):
            # Check for a winner
            if is_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {player_names[current_player]} wins!")
                continue_game = False

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                continue_game = False

            # Switch to the other player
            current_player = 1 - current_player
        else:
            print("Cell is already occupied. Choose another cell.")

if __name__ == "__main__":
    pass
    # Usage:
    # Uncomment the line below to start playing the game
    #play_tic_tac_toe()
    # doctest.testmod()

s = "sld"
print(s[:-1])





            

        

            
            



    


