
import numpy as np
import sys


# max requirement of each process for each resource ( one row dedicated to each process)
claimMatrix = np.array([
    [3,2,2],
    [6,1,3],
    [3,1,4],
    [4,2,2]
])

# current allocation for each process
allocMatrix = np.array([
    [2,0,1],
    [5,1,1],
    [2,1,1],
    [0,0,2]
])


resourceVector = np.array([9,3,6])
availableVector = np.array([0,1,1])
cMinusA = np.subtract(claimMatrix, allocMatrix)
processRowValid = False # init set to false so we can check first row w/o getting sucked into updateForNextState method
rowNotZero = True



def processState(claimMatrix, allocMatrix, cMinusA, availableVector, processRowValid):
    for i in range(len(claimMatrix) + 1): 
        if(processRowValid):
            updateForNextState(resourceVector, availableVector, allocMatrix, cMinusA, claimMatrix, i)
            

        processRow = np.subtract(cMinusA[i-1], availableVector)
        # step through process row to make sure all indexes are <= 0
        processRowValid = True
        for j in range(len(processRow)):
            if(processRow[j] > 0):
                processRowValid = False # if we get all the way to the end of the row with no positives, switch this to a valid process 
                break
          




def updateForNextState(resourceVector, availableVector, allocMatrix, cMinusA, claimMatrix, i):
  
    availableVector = np.add(allocMatrix[i-1], availableVector) # updates available vector
    if (np.array_equal(availableVector, resourceVector)): # if available vector and resource vecotor match, then we know we have enough resources available to use
        print("This is a safe state")
        sys.exit()
    elif (np.array_equal(np.add(allocMatrix, allocMatrix), allocMatrix) and not np.array_equal(claimMatrix, allocMatrix)): # checks to see if the allocation matrix is zeroed out and the claim matrix isn't, implying there aren't enough resources to execute the processes properly.
        print("This is an unsafe state")
        sys.exit()
    else:
        cMinusA = np.delete(cMinusA, i-1, 0) # deletes the row that we've just processed
        allocMatrix = np.delete(allocMatrix, i-1, 0)
        claimMatrix = np.delete(claimMatrix, i-1, 0)
        processState(claimMatrix, allocMatrix, cMinusA, availableVector, processRowValid) # recursively begin the next iteration usng the updated matrices
    

processState(claimMatrix, allocMatrix, cMinusA, availableVector, processRowValid)
