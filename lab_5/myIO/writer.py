from typing import TextIO 
 
 
def write(output_file: TextIO, X, Y, eps): 
    for i in range(len(X)): 
        output_file.write(f"x[{i}]={X[i]}\ty[{i}]={Y[i]}\n") 
    output_file.write(f"eps={eps}") 
 
# f = open('output.txt', 'w') 
# X = [0,1,2,3] 
# Y = [0,1,4,9] 
# eps = 0.025 
# write(f, X, Y, eps) 