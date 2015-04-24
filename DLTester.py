"""
File to test DancingLink implmentation
"""
from DancingLink import DancingLink

dl = DancingLink()
print("Empty DL:\n" + dl.toString())

dl.addColumn("A")
dl.addColumn("B")
dl.addColumn("C")
dl.addColumn("D")
dl.addColumn("E")
dl.addColumn("F")
dl.addColumn("G")

dl.addRow([0,0,1,0,1,1,0])
dl.addRow([1,0,0,1,0,0,1])
dl.addRow([0,1,1,0,0,1,0])
dl.addRow([1,0,0,1,0,0,0])
dl.addRow([0,1,0,0,0,0,1])
dl.addRow([0,0,0,1,1,0,1])
print("Filled DL:\n" + dl.toString())

arr = [[0,0,1,0,1,1,0], [1,0,0,1,0,0,1], [0,1,1,0,0,1,0],[1,0,0,1,0,0,0],[0,1,0,0,0,0,1],[0,0,0,1,1,0,1]]
names = ["A", "B", "C", "D", "E", "F", "G"]
dl2 = DancingLink(arr, names)
print("Arr created DL:\n" + dl2.toString())
