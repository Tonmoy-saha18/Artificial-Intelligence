# This part is for priority queue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty or not
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].fn < self.queue[min].fn:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()


# This is our per node object part
class Node(object):
    def __init__(self, cur_node, gn, fn, obj):
        self.cur_node = cur_node
        self.gn = gn
        self.fn = fn
        self.prev_node = obj


# Here we initialize the graph and huristic function
queue = PriorityQueue()
node_track = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
hn = [7, 6, 2, 1, 0]
graph = [[0, 1, 4, 0, 0],
         [0, 0, 2, 5, 12],
         [0, 0, 0, 2, 0],
         [0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0]
         ]
total_cost = 0 + hn[0]
node = Node(0, 0, total_cost, None)
queue.insert(node)

#This part will done the main work for A* search
while not queue.isEmpty():
    extract_node = queue.delete()
    current_node = extract_node.cur_node
    prev_cost = extract_node.gn
    huristic_cost = hn[current_node]
    prev_node = extract_node.prev_node

    if current_node == 4:
        print_list = []
        total_cost = extract_node.gn
        print_list.append(node_track[extract_node.cur_node])
        while extract_node.prev_node is not None:
            extract_node = extract_node.prev_node
            print_list.append(node_track[extract_node.cur_node])
        path = ''
        count = 0
        for a in print_list.__reversed__():
            if count < len(print_list)-1:
                path = path + a + ' --> '
            else:
                path += a
            count += 1

        print('The path is: ', path)
        print('Total cost is:', total_cost)
        break
    else:
        track = 0
        for a in graph[current_node]:
            if a != 0:
                cur_node = track
                gn = prev_cost + a
                fn = gn + hn[track]
                previous_node = extract_node
                node = Node(cur_node, gn, fn, previous_node)
                queue.insert(node)
            track += 1
