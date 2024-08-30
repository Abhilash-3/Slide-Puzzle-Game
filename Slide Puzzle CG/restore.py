# import pygame
# import random
# import pyautogui
# import time
#
# class Tiles:
#     def __init__(self, screen, start_position_x, start_position_y, num, mat_pos_x, mat_pos_y):
#         # Initializes tile properties including position, number, and whether it's selected or movable
#         self.color = (0, 0, 0)  # Initial color of the tile (black)
#         self.screen = screen
#         self.start_pos_x = start_position_x
#         self.start_pos_y = start_position_y
#         self.num = num
#         self.width = tile_width
#         self.depth = tile_depth
#         self.selected = False
#         self.position_x = mat_pos_x
#         self.position_y = mat_pos_y
#         self.movable = False
#
#     def draw_tyle(self):
#         # Draws the tile on the screen
#         pygame.draw.rect(self.screen, self.color, pygame.Rect(
#             self.start_pos_x, self.start_pos_y, self.width, self.depth))
#         numb = font.render(str(self.num), True, (45, 45, 45))  # Number color (dark grey)
#         screen.blit(numb, (self.start_pos_x + 40, self.start_pos_y + 10))
#
#     def mouse_hover(self, x_m_motion, y_m_motion):
#         # Changes the tile's color when the mouse hovers over it
#         if x_m_motion > self.start_pos_x and x_m_motion < self.start_pos_x + self.width and y_m_motion > self.start_pos_y and y_m_motion < self.start_pos_y + self.depth:
#             self.color = (58, 58, 58)  # Hover color (dark grey)
#         else:
#             self.color = (0, 0, 0)  # Default color (black)
#
#     def mouse_click(self, x_m_click, y_m_click):
#         # Selects the tile if it is clicked
#         if x_m_click > self.start_pos_x and x_m_click < self.start_pos_x + self.width and y_m_click > self.start_pos_y and y_m_click < self.start_pos_y + self.depth:
#             self.selected = True
#         else:
#             self.selected = False
#
#     def mouse_click_release(self, x_m_click_rel, y_m_click_rel):
#         # Deselects the tile when the mouse click is released
#         if x_m_click_rel > 0 and y_m_click_rel > 0:
#             self.selected = False
#
#     def move_tyle(self, x_m_motion, y_m_motion):
#         # Moves the tile's position on the screen based on mouse movement
#         self.start_pos_x = x_m_motion
#         self.start_pos_y = y_m_motion
#
#
# def create_tyles():
#     # Creates tiles with random numbers, excluding one tile for the empty space
#     i = 1
#     while i <= tile_count:
#         r = random.randint(1, tile_count)
#         if r not in tile_no:
#             tile_no.append(r)
#             i += 1
#     tile_no.append("")  # Add an empty tile at the end
#     k = 0
#     for i in range(0, rows):
#         for j in range(0, cols):
#             if (i == rows - 1) and (j == cols - 1):
#                 pass  # Skip the last tile which is empty
#             else:
#                 t = Tiles(screen, tile_print_position[(i, j)][0], tile_print_position[(i, j)][1], tile_no[k], i, j)
#                 tiles.append(t)
#             matrix[i][j] = tile_no[k]
#             k += 1
#     check_mobility()
#
#
# def check_mobility():
#     # Checks and updates which tiles are movable based on their positions relative to the empty space
#     for i in range(tile_count):
#         tile = tiles[i]
#         row_index = tile.position_x
#         col_index = tile.position_y
#         adjacent_cells = []
#         adjacent_cells.append([row_index - 1, col_index, False])  # Up
#         adjacent_cells.append([row_index + 1, col_index, False])  # Down
#         adjacent_cells.append([row_index, col_index - 1, False])  # Left
#         adjacent_cells.append([row_index, col_index + 1, False])  # Right
#         for i in range(len(adjacent_cells)):
#             if (adjacent_cells[i][0] >= 0 and adjacent_cells[i][0] < rows) and (
#                     adjacent_cells[i][1] >= 0 and adjacent_cells[i][1] < cols):
#                 adjacent_cells[i][2] = True
#
#         for j in range(len(adjacent_cells)):
#             if adjacent_cells[j][2]:
#                 adj_cell_row = adjacent_cells[j][0]
#                 adj_cell_col = adjacent_cells[j][1]
#                 for k in range(tile_count):
#                     if adj_cell_row == tiles[k].position_x and adj_cell_col == tiles[k].position_y:
#                         adjacent_cells[j][2] = False
#
#                 false_count = 0
#
#                 for m in range(len(adjacent_cells)):
#                     if adjacent_cells[m][2]:
#                         tile.movable = True
#                         break
#                     else:
#                         false_count += 1
#
#                 if false_count == 4:
#                     tile.movable = False
#
#
# def isGameOver():
#     # Checks if the game is over either by completing the puzzle or reaching the maximum number of moves
#     global game_over, game_over_banner
#     allcelldata = ""
#     for i in range(rows):
#         for j in range(cols):
#             allcelldata = allcelldata + str(matrix[i][j])
#
#     if allcelldata == "12345678 ":
#         game_over = True
#         game_over_banner = f"Congratulations! Moves: {move_count}"
#         print("Congratulations! Puzzle completed.")
#
#         for i in range(tile_count):
#             tiles[i].movable = False
#             tiles[i].selected = False
#     elif move_count >= MAX_MOVES:
#         game_over = True
#         game_over_banner = f"Game Over! Maximum moves ({MAX_MOVES}) reached."
#         print("Game Over! Maximum moves reached.")
#
#         for i in range(tile_count):
#             tiles[i].movable = False
#             tiles[i].selected = False
#
#
# # Define the maximum number of moves allowed
# MAX_MOVES = 50
#
# # Window dimension
# page_width, page_depth = pyautogui.size()
# page_width = int(page_width * .95)
# page_depth = int(page_depth * .95)
#
# # Tile dimensions
# tiles = []
# tile_width = 200
# tile_depth = 200
#
# # Number of rows & columns (puzzle size)
# rows, cols = (3, 3)
# tile_count = rows * cols - 1  # How many tiles should be created
# matrix = [["" for i in range(cols)] for j in range(rows)]
# tile_no = []
# tile_print_position = {(0, 0): (100, 50),
#                        (0, 1): (305, 50),
#                        (0, 2): (510, 50),
#                        (1, 0): (100, 255),
#                        (1, 1): (305, 255),
#                        (1, 2): (510, 255),
#                        (2, 0): (100, 460),
#                        (2, 1): (305, 460),
#                        (2, 2): (510, 460)}
#
# # Initial values of variables
# mouse_press = False
# x_m_click, y_m_click = 0, 0
# x_m_click_rel, y_m_click_rel = 0, 0
# game_over = False
# game_over_banner = ""
# move_count = 0
#
# # Timer variables
# start_time = time.time()
# total_time = 3 * 60  # 3 minutes in seconds
#
# # Initialize pygame and set the caption
# pygame.init()
# game_over_font = pygame.font.Font('freesansbold.ttf', 70)  # Font for the "Game Over" message
# move_count_banner = "Moves : "
# move_count_font = pygame.font.Font('freesansbold.ttf', 40)  # Font for the move count
# timer_font = pygame.font.Font('freesansbold.ttf', 40)  # Font for the timer
# screen = pygame.display.set_mode((page_width, page_depth))
# pygame.display.set_caption("Slide Game")
# font = pygame.font.Font('freesansbold.ttf', 200)  # Font for tile numbers
#
# # Title font and text
# title_font = pygame.font.Font('freesansbold.ttf', 100)  # Font for the title
# title_text = title_font.render('THE PUZZLE', True, (165, 42, 42))  # Title text color
#
#
# # Snowflake functions
# def initialize_snowflakes(num_snowflakes):
#     # Initializes snowflakes with random positions and speeds
#     snowflakes = []
#     for _ in range(num_snowflakes):
#         x_pos = random.randint(0, page_width)
#         y_pos = random.randint(0, page_depth)
#         speed = random.uniform(0.5, 1.5)  # Reduced speed
#         snowflakes.append([x_pos, y_pos, speed])
#     return snowflakes
#
#
# def update_snowflakes(snowflakes):
#     # Updates the position of each snowflake and resets them if they go off-screen
#     for snowflake in snowflakes:
#         snowflake[0] += snowflake[2]  # Move snowflake to the right
#         snowflake[1] += snowflake[2]  # Move snowflake downwards
#         if snowflake[0] > page_width:
#             snowflake[0] = random.randint(0, page_width)
#             snowflake[1] = random.randint(0, page_depth)
#         if snowflake[1] > page_depth:
#             snowflake[0] = random.randint(0, page_width)
#             snowflake[1] = random.randint(0, page_depth)
#
#
# # Initialize snowflakes
# snowflakes = initialize_snowflakes(100)  # Adjust the number of snowflakes as needed
#
# # Creation of tiles in the puzzle
# create_tyles()
#
# running = True
# while running:
#     screen.fill((0, 0, 0))  # Fill the background with black color
#
#     # Draw the snowflakes
#     update_snowflakes(snowflakes)
#     for snowflake in snowflakes:
#         pygame.draw.circle(screen, (255, 255, 255), (int(snowflake[0]), int(snowflake[1])),
#                            2)  # Snowflake color (white)
#
#     # Draw the puzzle board
#     pygame.draw.rect(screen, (165, 42, 42), pygame.Rect(95, 45, 620, 620))  # Draw the puzzle board (brownish-red)
#
#     # Blit the title
#     screen.blit(title_text, (page_width // 2 - title_text.get_width() // 2 + 260, 10))  # Center the title at the top
#
#     # Render the game over banner if the game is over
#     game_over_print = game_over_font.render(game_over_banner, True, (255, 255, 0))  # Game over banner color (yellow)
#     screen.blit(game_over_print, (200, 800))  # Adjusted to move towards the left
#
#     # Render the move count
#     if move_count == 0:
#         move_count_render = move_count_font.render(move_count_banner, True,
#                                                    (45, 45, 45))  # Initial move count color (dark grey)
#     else:
#         move_count_render = move_count_font.render(f"{move_count_banner} {move_count}", True,
#                                                    (79, 79, 79))  # Move count color (grey)
#     screen.blit(move_count_render, (1050, 200))
#
#     # Calculate the remaining time
#     elapsed_time = time.time() - start_time
#     remaining_time = total_time - elapsed_time
#
#     # Check if time is up
#     if remaining_time <= 0:
#         remaining_time = 0
#         game_over = True
#         game_over_banner = "Time's Up!"
#         for i in range(tile_count):
#             tiles[i].movable = False
#             tiles[i].selected = False
#
#     # Render the timer
#     mins, secs = divmod(remaining_time, 60)
#     timer_display = f"Time: {int(mins):02}:{int(secs):02}"
#     timer_render = timer_font.render(timer_display, True, (255, 255, 255))  # Timer color (white)
#     screen.blit(timer_render, (1050, 300))
#
#     # Get events from the queue
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEMOTION:
#             x_m_motion, y_m_motion = pygame.mouse.get_pos()
#             for i in range(tile_count):
#                 tiles[i].mouse_hover(x_m_motion, y_m_motion)
#             for i in range(tile_count):
#                 if tiles[i].selected and mouse_press:
#                     tiles[i].move_tyle(x_m_motion, y_m_motion)
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_press = True
#             x_m_click, y_m_click = pygame.mouse.get_pos()
#             for i in range(tile_count):
#                 tiles[i].mouse_click(x_m_click, y_m_click)
#         if event.type == pygame.MOUSEBUTTONUP:
#             mouse_press = False
#             x_m_click_rel, y_m_click_rel = pygame.mouse.get_pos()
#             x_m_click, y_m_click = 0, 0
#             cell_found = False
#             for i in range(0, rows):
#                 for j in range(0, cols):
#                     tile_start_pos_x = tile_print_position[(i, j)][0]
#                     tile_start_pos_y = tile_print_position[(i, j)][1]
#
#                     if (x_m_click_rel > tile_start_pos_x and x_m_click_rel < tile_start_pos_x + tile_width) and (
#                             y_m_click_rel > tile_start_pos_y and y_m_click_rel < tile_start_pos_y + tile_depth):
#                         if matrix[i][j] == "":
#                             for k in range(tile_count):
#                                 if not game_over:
#                                     if tiles[k].selected:
#                                         if tiles[k].movable:
#                                             cell_found = True
#                                             dummy = matrix[tiles[k].position_x][tiles[k].position_y]
#                                             matrix[tiles[k].position_x][tiles[k].position_y] = matrix[i][j]
#                                             matrix[i][j] = dummy
#                                             tiles[k].position_x = i
#                                             tiles[k].position_y = j
#                                             tiles[k].start_pos_x = tile_print_position[(
#                                                 i, j)][0]
#                                             tiles[k].start_pos_y = tile_print_position[(
#                                                 i, j)][1]
#                                             move_count += 1
#                                             isGameOver()
#                                             check_mobility()
#
#                     if not cell_found:
#                         for k in range(tile_count):
#                             if tiles[k].selected:
#                                 mat_pos_x = tiles[k].position_x
#                                 mat_pos_y = tiles[k].position_y
#                                 tiles[k].start_pos_x = tile_print_position[(
#                                     mat_pos_x, mat_pos_y)][0]
#                                 tiles[k].start_pos_y = tile_print_position[(
#                                     mat_pos_x, mat_pos_y)][1]
#                                 break
#
#     for i in range(tile_count):
#         tiles[i].draw_tyle()  # Draw all tiles
#     pygame.display.flip()  # Update the portion of the screen where changes occurred
#
# pygame.display.update()  # Update the entire screen
# pygame.quit()
