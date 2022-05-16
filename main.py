# LOW_RANGE =-100
# HIGH_RANGE = 100
from matrix import Matrix


WELCOME_MSG = "Welcome to the Matrix Flatten Program!\n"
def main():

    print("Enter Matrix Dimensions: ")
    flag = True
    while flag:
        try :
            N = int(input('N = ').strip())
            M = int(input('M = ').strip())
            P = int(input('P = ').strip())
            flag = False
        except ValueError:
            print("Invalid input. Please try again.")
            flag = True
            
    print("\n")
    matrix = Matrix(N,M,P)
    matrix.flatten_matrix()

    print("Matrix Created...")
    show_matrix_q = input("Do you want to display the matrix? (y/n)")
    if show_matrix_q == 'y':
        print(matrix.matrix)
    print("\n")

    print("Matrix Flattened...")
    matrix.flatten_matrix()
    print("Matrix Flattened lenght = ", len(matrix.matrix_flattend))

    show_matrix_q = input("Do you want to display the flattened matrix? (y/n)")
    if show_matrix_q == 'y':
        print(matrix.matrix_flattend)
    print("\n")

    
    flag = True
    while flag:

        try:
            i = int(input("Enter the index i: ").strip())
            j = int(input("Enter the index j: ").strip())
            k = int(input("Enter the index k: ").strip())
    
            index = matrix.get_1D_index_from_3D(i,j,k)

            item =matrix.get_item_from_flatten_by_index(index)
            print("Flattened matrix : The item at index {} is: {}".format(index, item))

            item =matrix.get_item_from_3d_by_index(i,j,k)
            print("Original matrix : The item at index {},{},{} is: {}".format(i,j,k, item))
            flag = False
        except IndexError:
            print("Error : Index out of range")
            print('Please Try again..')
            flag = True
        except ValueError:
            print("Error : Invalid input. Please try again.")
            print('Please Try again..')
            flag = True


if __name__ == "__main__":
    main()