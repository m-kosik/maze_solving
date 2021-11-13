
import matplotlib.pyplot as plt

def check_path(maze):
    solver = Solver(maze)
    width = solver.maze.shape[0]
    length = solver.maze.shape[1]
    while True:
        solver.make_one_move()
        solver.show_maze()
        if solver.is_game_stuck:
            if solver.current_position == (width-1,length-1):
                return True
            else:
                return False
        if solver.current_position == (0,0) and not solver.available_start_directions:
            return False
        if solver.current_position == (width-1,length-1):
            return True

class Solver():
    def __init__(self, maze, start_position = (0,0), end_position = None, direction = 'S'):
        self.maze = maze
        self.current_position = start_position
        self.direction = direction
        if not end_position:
            self.end_position = (self.maze.shape[0]-1, self.maze.shape[1]-1)
        self.is_game_stuck = False
        self.available_start_directions = ['W','S']

    def make_one_move(self):
        temp_checked = []
        if self.current_position == (0,0):
            self.direction = self.available_start_directions[0]
            self.available_start_directions.remove(self.direction)
        else:
            start_checking_in_direction = {'W':'E', 'N':'S', 'E':'W', 'S':'N'}
            self.direction = start_checking_in_direction[self.direction]
        
        while True:
            self.set_new_direction()
            new_position = self.find_new_position()
            if self.is_move_valid(new_position) and not self.maze[new_position]:
                self.current_position = new_position
                break
            elif 'W' in temp_checked and 'E' in temp_checked and 'S' in temp_checked and 'N' in temp_checked:
                self.is_game_stuck = True
                break
            else:
                temp_checked.append(self.direction)

    def find_new_position(self):
        if self.direction == 'N':
            new_position = (self.current_position[0]-1, self.current_position[1])
        elif self.direction == 'E':
            new_position = (self.current_position[0], self.current_position[1]+1)
        elif self.direction == 'S':
            new_position = (self.current_position[0]+1, self.current_position[1])
        elif self.direction == 'W':
            new_position = (self.current_position[0], self.current_position[1]-1)
        else:
            print('The direction should be a single letter chosen from: N,E,S,W.')
        return new_position

    def is_move_valid(self,position):
        horizontal_size = len(self.maze[0])
        vertical_size = len(self.maze)
        if (position[1] == -1 or position[1] == horizontal_size 
        or position[0] == -1 or position[0] == vertical_size):
            return False
        else:
            return True
    
    def set_new_direction(self):
        directions_clockwise = {'W':'S', 'N':'W', 'E':'N', 'S':'E'}
        self.direction = directions_clockwise[self.direction]

    def show_maze(self):
        if self.direction == 'N':
            marker = "^"
        elif self.direction == 'S':
            marker = "v"
        elif self.direction == 'E':
            marker = ">"
        elif self.direction == 'W':
            marker = "<"
        fig = plt.subplots(figsize = [2,2])
        plt.imshow(self.maze, cmap = 'bone_r')
        plt.scatter(self.current_position[1],self.current_position[0],marker=marker,c='red',s=100)
        plt.show()
    



# def string_to_array(input_str):
#     maze_width = input_str.find('\n')
#     maze_length = input_str.count('\n') + 1
#     input_str = input_str.replace('W','1,')
#     input_str = input_str.replace('.','0,')
#     maze_array = np.fromstring(input_str, sep=',').reshape(maze_width,maze_length)
#     return maze_array