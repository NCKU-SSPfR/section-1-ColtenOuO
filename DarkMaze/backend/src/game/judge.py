import numpy as np
import re
import json

def _parse_map(map_string, map_size, reversal_nodes=[]):
    width, height = map_size
    filtered_chars = re.sub(r'[^a-zA-Z]', '', map_string)
    
    QQ = [bin(ord(c))[2:].zfill(8) for c in filtered_chars]
    
    Dora_friend = []
    for Q in QQ:
        first_half = int(Q[:4], 2)
        second_half = int(Q[4:], 2)
        Dora_friend.extend([first_half % 2, second_half % 2])
    
    while len(Dora_friend) < width * height:
        Dora_friend.append(0)
    
    Dora_friend = Dora_friend[:width * height]
    
    swiper = np.array(Dora_friend).reshape((height, width))
    
    for x, y in reversal_nodes:
        if 0 <= x < height and 0 <= y < width:
            swiper[y, x] = 1 - swiper[y, x]
    
    return swiper

def _load_maze_from_json(maze_level_name):
    with open("./src/game/maze_level/" + maze_level_name + ".json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    maze_level_name = data.get("maze_level_name", "Unknown Level")
    map_size = tuple(data.get("map_size", [10, 10]))
    starting_position = tuple(data.get("starting_position", [0, 0]))
    end_position = tuple(data.get("end_position", [0, 0]))
    map_string = data.get("map", "")
    reversal_nodes = data.get("reversal_node", [])
    
    parsed_map = _parse_map(map_string, map_size, reversal_nodes)
    
    return {
        "maze_level_name": maze_level_name,
        "map_size": map_size,
        "starting_position": starting_position,
        "end_position": end_position,
        "map": parsed_map
    }

def hit_obstacle(position, maze_level_name):
    x, y = position
    maze_data = _load_maze_from_json(maze_level_name)  # You can replace this with the actual level you're working with
    grid = maze_data["map"]
    
    # Check if the position is within the bounds of the grid
    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        # Return True if there's an obstacle (1) at the position, False if free space (0)
        return grid[y, x] == 1
    else:
        # Position is out of bounds
        return True

def game_over(health):
    if health == 0 or health == 666:
        return True
    
    return False

def arrive_at_destination(maze_level_name, current_position):
    with open("./src/game/maze_level/" + maze_level_name + ".json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    end_position = tuple(data.get("end_position", [0, 0]))
    if tuple(current_position) == end_position:
        return True
    
    return False
