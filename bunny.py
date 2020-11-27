import numpy as np
import argparse

def bunny_start_position(A, N, M):
    '''
    this function find the initial position of Bunny
    argument:
    A: the matrix
    N: number of rows
    M: number of columns
    '''
	if N%2==1 and M%2==1:
		return ((N//2) , (M//2))
	elif N%2==1:
		if A[N/2][M/2]>=A[N/2][M/2+1]:
			return ((N//2) , M/2)
		else:
			return ((N//2) , (M/2)-1)
	elif M%2==1:
		if A[N/2][M/2]>A[N/2+1, M/2]:
			return (N/2, (M//2) )
		else:
			return ((N/2)-1, (M//2) )
	else:
		maximum = np.argmax([A[N/2][M/2], A[N/2][(M/2) -1], A[(N/2) - 1][M/2], A[(N/2) - 1][(M/2) -1]])
		if maximum==0:
			return (N/2,M/2)
		elif maximum==1:
			return (N/2, (M/2) -1)
		elif maximum==2:
			return ((N/2)-1, M/2)
		else:
			return ((N/2)-1, (M/2) -1)

def update_bunny_position(A, bunny_i, bunny_j):
	'''
	this function find the next position for Bunny
	arguments:
	A: the matrix
	bunny_i: Bunny's current row
	bunny_j: Bunny's current columns
	'''
	maximum = 0
	index_max = (bunny_i, bunny_j)

	try:
		if bunny_i - 1<0:
			raise ValueError('Stop')
		elif bunny_j - 1<0:
			raise ValueError('Stop')
		elif A[bunny_i-1][bunny_j]>=maximum:
			maximum=A[bunny_i - 1][bunny_j]
			index_max=(bunny_i - 1, bunny_j)
	except:
		pass

	try:
		if bunny_i<0:
			raise ValueError('Stop')
		elif bunny_j - 1<0:
			raise ValueError('Stop')
		elif A[bunny_i][bunny_j-1]>=maximum:
			maximum=A[bunny_i ][bunny_j -1]
			index_max=(bunny_i, bunny_j -1)
	except:
		pass

	try:
		if bunny_i+1<0:
			raise ValueError('Stop')
		elif bunny_j<0:
			raise ValueError('Stop')
		elif A[bunny_i+1][bunny_j]>=maximum:
			maximum=A[bunny_i + 1][bunny_j]
			index_max=(bunny_i + 1, bunny_j)
	except:
		pass

	try:
		if bunny_i<0:
			raise ValueError('Stop')
		elif bunny_j + 1<0:
			raise ValueError('Stop')
		elif A[bunny_i][bunny_j+1]>=maximum:
			maximum=A[bunny_i ][bunny_j+1]
			index_max=(bunny_i , bunny_j+1)
	except:
		pass

	return (maximum, index_max)

	



def garden (N, M, C): 
    '''
    this function make Bunny's path
    Argument:
    N is the number of rows
    M the number of column of the matrix
    C is the maximum number of carrot in a case

    Output:Number of carrots and initial matrix
    '''
    A = np.random.randint(C, size=(N, M)) # Creation of a random matrix with the number of carrots 
    A_depart = A.copy()
    bunny_i, bunny_j = bunny_start_position(A, N, M)

    new_carrot = A[bunny_i][bunny_j] + 1
    total_carrots = new_carrot - 1
    print(total_carrots)
    print(bunny_i, bunny_j)
    A[bunny_i][bunny_j] = 0
    while new_carrot>0:
        (new_carrot, (i, j)) = update_bunny_position(A, bunny_i, bunny_j)
        print(new_carrot)
    	print(total_carrots)
        bunny_i = i
        bunny_j = j
        print(bunny_i, bunny_j)
        if new_carrot>0:
            A[bunny_i][bunny_j] = 0
        total_carrots+=new_carrot
    return total_carrots, A_depart


if __name__ == '__main__':
    prs = argparse.ArgumentParser()
    prs.add_argument('-N', '--rows', help='Number of rows', type=int, default=5)
    prs.add_argument('-M', '--columns', help='Number of columns', type=int, default=5)
    prs.add_argument('-C', '--max_carrots', help='maximum number of carrots in a case', type=int, default=15)
    prs = prs.parse_args()
    total_carrots, A_depart = garden(prs.rows, prs.columns, prs.max_carrots)
    print('Bunny has just ate ', total_carrots, ' carrots. \n')
    print('Initial matrix: ', A_depart)
    


