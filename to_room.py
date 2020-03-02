from util import Queue

def bfs(start, map, destination):
        
        queue = Queue()
        
        visited = set()
        # add the path to the starting room (including entire room) to the queue
        queue.enqueue([start])
        
        while queue.size() > 0:
        
            path = queue.dequeue()
            # removed the last (entire) room from the queue
            room = path[-1]
            
            if room == destination:
                return path
            elif room not in visited:
                visited.add(room)
                # get adjacent edges and add to back of path by pulling neighbors from the room object
                neighbors = room.neighbors
                for neighbor in neighbors:
                    # make a copy of the path
                    new_path = path.copy()
                    # add neighbor to the back of that path
                    new_path.append(neighbor)
                    # add the path to the queue
                    queue.enqueue(new_path)