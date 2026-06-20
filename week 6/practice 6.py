from collections import deque 

queue = deque() 

queue.append('A') 
queue.append('B') 
queue.append('C') 
print('Queue:', queue) 

front = queue[0]
print('Peek:', front)

keluar = queue.popleft() 
print('Dequeue:', keluar)
print('Queue:', queue) 

print('Kosong?', len(queue)==0)
print('Ukuran:', len(queue))