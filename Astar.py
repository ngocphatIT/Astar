class Node:
    def __init__(self,parent=None,position=None):
        self.parent=parent
        self.position=position
        self.g=0
        self.h=0
        self.f=0
    def __eq__(self,other):
        return self.position==other.position
def astar(data,start,goal):
    start_node=Node(None,start)
    end_node=Node(None,goal)
    open_list=[]
    closed_list=[]
    open_list.append(start_node)
    while len(open_list)>0:
        current_node=open_list[0]
        current_index=0
        for index, item in enumerate(open_list):
            if item.f<current_node.f:
                current_node=item
                current_index=index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node==end_node:
            path=[]
            current=current_node
            while current is not None:
                path.append(current.position)
                current=current.parent
            return path[::-1]
        children=[]
        for new_position in [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            node_position=(current_node.position[0]+new_position[0],current_node.position[1]+new_position[1])
            if node_position[0]<=len(data)-1 and node_position[0]>=0 and node_position[1]<=len(data[0])-1 and node_position[1]>=0:
                if data[node_position[0]][node_position[1]]!=1:
                    new_node=Node(current_node,node_position)
                    children.append(new_node)
        for child in children:
            if child not in closed_list:
                child.g=current_node.g+1
                child.h=((child.position[0]-end_node.position[0])**2+((child.position[1]-end_node.position[1])**2))
                child.f=child.g+child.h
                for open_node in open_list:
                    if child==open_node and child.g>open_node.g:
                        continue
                open_list.append(child)
if __name__ == '__main__':
    maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    start = (0, 0)
    goal = (8, 9)

    path = astar(maze, start, goal)
    print(path)          
