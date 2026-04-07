import numpy as np
A = np.array([[4, 4, 6],
              [1, 1, 2],
              [1, 2, 4]])

b = np.array([460, 130, 240])

y = np.linalg.det(A)
if y != 0:
    print("Матриця A є невиродженою.")
else:    
    print("Матриця A є виродженою.")
print("Determinant matrix A:", round(y, 2))

x = np.linalg.solve(A, b)
print("Solution of the system:", x)

Verification = np.dot(A, x)
if np.allclose(Verification, b):
    print("Verification successful: A @ x is approximately equal to b.")    
else:
    print("Verification failed: A @ x is not approximately equal to b.")     

print("\nSolution:")
print("Розвідник:", int(round(x[0])))
print("Камікадзе:", int(round(x[1])))
print("Вантажний:", int(round(x[2])))





