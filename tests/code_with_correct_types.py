from src.simple_pipe import Pipe

input_A = (1, 2, 3)
input_B = ["sasquatch"]

function_A = Pipe | list | reversed | iter | next
result_A = function_A(input_A)

function_B = Pipe | iter | next | len
result_B = function_B(input_B)
