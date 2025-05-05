import doctest

def initialize_board() -> list[list[str]]:
    """ 
    Initialize the game board as a 3x3 nested list. 
    
    
    >>> initialize_board()
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    """
    initial_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return initial_board

# This function is provided, and you can leave it as is.
def return_board(board: list[list[str]]) -> None:
    """
    return the current state of the game board.
    
    >>> return_board([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    >>> return_board([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])
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
    
    >>> drop_piece([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']], 0, 1, 'X')
    False
    >>> drop_piece([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']], 2, 2, 'X')
    False
    >>> drop_piece([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']], 1, 0, 'X')
    True
    """
    return board[row][col] == ' '

def is_winner(board: list[list[str]], player: str) -> bool:
    """
    Check if a player has won the game. A player win the game if the pieces placed by the player are in row, columns or diagonals

    Returns:
    - bool: True if the player has won, False otherwise.
    
    >>> is_winner([[' ', 'X', ' '], ['O', 'X', ' '], [' ', 'X', 'O']], 'X')
    True
    >>> is_winner([[' ', 'X', ' '], ['O', 'X', ' '], [' ', 'X', 'O']], 'O')
    False
    >>> is_winner([['X', 'X', 'X'], ['O', ' ', ' '], [' ', ' ', 'O']], 'X')
    True
    >>> is_winner([['X', 'X', 'X'], ['O', ' ', ' '], [' ', ' ', 'O']], 'O')
    False
    >>> is_winner([['X', ' ', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']], 'X')
    True
    >>> is_winner([['X', ' ', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']], 'O')
    False
    """

    if player in board[0][0] and player in board[1][0] and player in board[2][0]:
        return(True)
    elif player in board[0][1] and player in board[1][1] and player in board[2][1]:
        return(True)
    elif player in board[0][2] and player in board[1][2] and player in board[2][2]:
        return(True)
    elif player in board[0][0] and player in board[0][1] and player in board[0][2]:
        return(True)
    elif player in board[1][0] and player in board[1][1] and player in board[1][2]:
        return(True)
    elif player in board[2][0] and player in board[2][1] and player in board[2][2]:
        return(True)
    elif player in board[0][0] and player in board[1][1] and player in board[2][2]:
        return(True)
    elif player in board[0][2] and player in board[1][1] and player in board[2][0]:
        return(True)
    else:
        return(False)

        
            

def is_board_full(board: list[list[str]]) -> bool:
    """ Check if the game board is full, indicating a tie if there is no winner.
    
    >>> is_board_full([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])
    False
    >>> is_board_full([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']])
    True
    """
    for row in board:
        for column in row:
            if column == ' ':
                return False
            return True

# This function is provided, and you can leave it as is.
def play_tic_tac_toe() -> None:
    """ Orchestrate the game, allowing two players to take turns."""
    # Initialize the game board
    board = initialize_board()

    # Define players
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    
    player_1_name = input("What is the name of player 1? ").strip()
    player_2_name = input("What is the name of player 2? ").strip()
    if not player_1_name:
        player_1_name = '1'
    if not player_2_name:
        player_2_name = '2'
        
    player_names = [player_1_name, player_2_name]
    
    continue_game = True

    while continue_game:
        return_board(board)

        # Get player input
        # As we are facing regular players, the row and col start 1 so that they don't get confused
        row = input(f"Player {player_names[current_player]}, choose a row (1/2/3): ").strip()
        col = input(f"Player {player_names[current_player]}, choose a column (1/2/3): ").strip()
        
        try:
            row = int(row) - 1
            col = int(col) - 1
            assert row in [0, 1, 2] and col in [0, 1, 2], "row and col must be an int ranged from 1, 2, 3"
        except:
            print("row and col must be an int ranged from 1, 2, 3")
            continue
        
        # Drop the player's piece into the chosen cell
        if drop_piece(board, row, col, players[current_player]):
            # Check for a winner
            if is_winner(board, players[current_player]):
                return_board(board)
                print(f"Player {player_names[current_player]} wins!")
                continue_game = False

            # Check for a tie
            if is_board_full(board):
                return_board(board)
                print("It's a tie!")
                continue_game = False

            # Switch to the other player
            current_player = 1 - current_player
        else:
            return("Cell is already occupied. Choose another cell.")

if __name__ == "__main__":
    # Usage:
    # Uncomment the line below to start playing the game
    # print(play_tic_tac_toe())
    doctest.testmod()
