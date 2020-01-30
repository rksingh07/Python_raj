# Python: Binary to Decimal Conversion
# binToDec and decToBin functions are rendered obsolete by the universal convert function


def binToDec(binNum):
        decNum = 0
        power = 0
        while binNum > 0:
                decNum += 2 ** power * (binNum % 10)
                binNum //= 10
                power += 1
        return decNum
        
def decToBin(decNum):
        binNum = 0
        power = 0
        while decNum > 0:
                binNum += 10 ** power * (decNum % 2)
                decNum //= 2
                power += 1
        return binNum
        
def convert(fromNum, fromBase, toBase):
        toNum = 0
        power = 0
        while fromNum > 0:
                toNum += fromBase ** power * (fromNum % toBase)
                fromNum //= toBase
                power += 1
        return toNum


# print (str(binToDec(101011)))
# print (str(decToBin(128)))
print (str(convert(127, 10, 8)))        # converts 127 in  base 10 to base 8
print (str(convert(101001, 2, 2)))


# Python: DepthFirstSearch.py

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.dfs(a)
g.print_graph()



# Hash Map

class HashMap:
        def __init__(self):
                self.size = 6
                self.map = [None] * self.size
		
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
		
        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
			
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
			
        def delete(self, key):
                key_hash = self._get_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False
	
        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr
			
        def print(self):
                print('---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))
			
h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()		
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
print(h.keys())



# Python MaxHeap
# public functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown

class MaxHeap:
	def __init__(self, items=[]):
		super().__init__()
		self.heap = [0]
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap) - 1)

	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
			
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else: 
			max = False
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index//2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))


# Temperature Conversion Program

def menu():
	print("\n1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("3. Exit")
	choice = int(input("Enter a choice: "))
	return choice
	
def toCelsius(f):
	return int((f - 32) / 1.8)

def toFahrenheit(c):
	return int(c * 1.8 + 32)
	
def main():
	choice = menu()
	while choice != 3:
		if choice == 1:
			c = eval(input("Enter degrees Celsius: "))
			print(str(c) + "C = " + str(toFahrenheit(c)) + "F")
		elif choice == 2:
			f = eval(input("Enter degrees Fahrenheit: "))
			print(str(f) + "F = " + str(toCelsius(f)) + "C")
		else:
			print("Invalid choice.")
		choice = menu()
		
main()

#factorial function
def get_recursive_factorial(n):
	if n < 0:
		return -1
	elif n < 2:
		return 1
	else:
		return n * get_recursive_factorial(n-1)
		
def get_iterative_factorial(n):
	if n < 0:
		return -1
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
		return fact
		
print(get_recursive_factorial(6))
print(get_iterative_factorial(6))
