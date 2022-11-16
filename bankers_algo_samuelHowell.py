# Samuel Howell
# 10/16/22
# Bankers Algorithm
# CS-410

def subtractMatrices(matrix_A, matrix_B):
    if isinstance(matrix_A, list): # check matrix A against the generic tuple list. If true, then reduce instance by returning recursive call
        return [
                subtractMatrices(row_a, row_b) 
                for row_a, row_b 
                in zip(matrix_A, matrix_B) # The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(), so each row from a is paired with each row from b
                ]
    else:
        return matrix_A - matrix_B


def addMatrices(matrix_A, matrix_B):
    if isinstance(matrix_A, list): # check matrix A against the generic tuple list. If true, then reduce instance by returning recursive call
        return [
                addMatrices(row_a, row_b) 
                for row_a, row_b 
                in zip(matrix_A, matrix_B) # The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(), , so each row from a is paired with each row from b
                ]
    else:
        return matrix_A + matrix_B


class State:
    #! NOT SAFE STATE
    # declare our hardcoded arrays
    ALLOCATION_ARRAY = [
        [1, 0, 0],
        [5, 1, 1],
        [2, 1, 1],
        [0, 0, 2]
    ]
    
    CLAIM_ARRAY = [
        [3, 2, 2],
        [6, 1, 3],
        [3, 1, 4],
        [4, 2, 2]
    ]
    AVAILABLE_VECTOR = [0, 1, 1]

    # #! SAFE STATE
    # # declare our hardcoded arrays
    # ALLOCATION_ARRAY = [
    #     [1, 0, 0],
    #     [6, 1, 2],
    #     [2, 1, 1],
    #     [0, 0, 2]
    # ]
    
    # CLAIM_ARRAY = [
    #     [3, 2, 2],
    #     [6, 1, 3],
    #     [3, 1, 4],
    #     [4, 2, 2]
    # ]
    # AVAILABLE_VECTOR = [0, 1, 1]
    NEED_ARRAY = subtractMatrices(CLAIM_ARRAY, ALLOCATION_ARRAY) # c minus a from the textbook
    
    


    def safe(self):
        processes = self.NEED_ARRAY
        available = self.AVAILABLE_VECTOR
        possible = True
        while possible:
            found = [
                    process for process in enumerate(processes) 
                    if all(
                            [
                            True    if resource >= 0 
                                    else False for resource in subtractMatrices(available, process[1])
                            ]
                        )
                    ]
            if found:
                available = addMatrices(available, self.ALLOCATION_ARRAY[found[0][0]])
                processes.remove(found[0][1]) # remove the process from the array, so we don't reevaluate it by accident
            else:
                possible = False
        return not processes

if(State().safe()):
    print("This is a safe state")
else:
    print("This is not a safe state")