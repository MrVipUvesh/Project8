import numpy as np

class DataAnalytics:
    def __init__(self, elems, cols, rows = 1, dim = 0):
        global done_arr
        self.arr = np.array(elems)
        if(rows > 1 and dim == 0):
            self.arr = self.arr.reshape(rows, cols)
        elif(rows == 1 and dim == 0):
            self.arr = self.arr.reshape(cols)
        elif(dim > 0):
            self.arr = self.arr.reshape(rows, cols, dim)
        done_arr = self.arr
        print("\nArray created successfully:")
        print(self.arr)

    def slindex(self, arrType):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = input("Enter your choice: ")

            if(arrType == 1):
                match choice:
                    case "1":
                        index = int(input("Enter index number: "))
                        print("\nElement at index you choosed:")
                        print(self.arr[index])
                    case "2":
                        startIndex = int(input("Enter starting index: "))
                        endIndex = int(input("Enter ending index: "))
                        print("\nSliced Array:")
                        print(self.arr[startIndex:endIndex])
                    case "3":
                        break
                    case _:
                        print("Invalid option")
            else:
                match choice:
                    case "1":
                        rowIndex = int(input("Enter index of row: "))
                        colIndex = int(input("Enter index of column: "))
                        print("\nElement at index you choosed:")
                        print(self.arr[rowIndex][colIndex])
                    case "2":
                        rowIndex = input("Enter the row range (start:end): ")
                        row = rowIndex.split(":")
                        for i,k in enumerate(row):
                            row[i] = int(k)
                        colIndex = input("Enter the column range (start:end): ")
                        col = colIndex.split(":")
                        for i,k in enumerate(col):
                            col[i] = int(k)                    
                        print("\nSliced Array:")
                        print(self.arr[row[0]:row[1], col[0]:col[1]])                    
                    case "3":
                        break
                    case _:
                        print("Invalid option")
                        continue
    def math_ope(self, arr1, arr2, row, col, operation, dim = 0):
        if(operation == "1"):
            arr = np.add(arr1, arr2)
            if not in_arr_rows:
                arr = arr.reshape(row, col)
            else:
                arr = arr.reshape(row, col, dim)
            return arr
        elif(operation == "2"):
            arr = np.subtract(arr1, arr2)
            if not in_arr_rows:
                arr = arr.reshape(row, col)
            else:
                arr = arr.reshape(row, col, dim)
            return arr
        elif(operation == "3"):
            arr = np.multiply(arr1, arr2)
            if not in_arr_rows:
                arr = arr.reshape(row, col)
            else:
                arr = arr.reshape(row, col, dim)
            return arr
        elif(operation == "4"):
            arr = np.divide(arr1, arr2)
            if not in_arr_rows:
                arr = arr.reshape(row, col)
            else:
                arr = arr.reshape(row, col, dim)
            return arr
    def combine(self, arr1, arr2, row, col, dim = 0):
        arr = np.vstack((arr1, arr2))
        if not in_arr_rows:
            arr = arr.reshape(row*2, col)
        else:
            arr = arr.reshape(row*2, col, dim)
        return arr
    def split(self, arr, row, col, dim = 0):
        if(row % 2 == 0):
            arr = np.array(arr)
            if not in_arr_rows:
                arr = arr.reshape(row, col)
            else:
                arr = arr.reshape(row, col, dim)
            arr = np.vsplit(arr, 2)
            return arr
        else:
            print("[Error: In order to split an array, the number of rows shoud be even]")

print("\nWelcome to the Numpy Analyzer!")
print("="*40)
print("Choose and operation")
in_arr_rows = None
arr_rows = 1
done_arr = None
transfer = []

while True:
    print("\nChoose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            while True:
                print("\nSelect the type of array to create:")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")
                print("4. Back to main menu")
                arr_choice = input("Enter your choice: ")
                match arr_choice:
                    case "1":
                        Onedim_arr = []
                        arr_cols = int(input("Enter number of elements: "))
                        if(arr_cols <= 1):
                            print("[Error: Number of elements can't be less than 2]")
                            break
                        nElements = arr_cols
                        elements = input(f"Enter {nElements} elements for the array separated by space: ")
                        if(len(elements.split()) < arr_cols):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(elements.split()) > nElements):
                            print(f"[Error: Number of elements can't be greater than {nElements}]")
                            break                        
                        transfer = elements.split(" ")
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        final_arr = transfer.copy()
                        transfer.clear()
                        da = DataAnalytics(final_arr, arr_cols)
                        da.slindex(1)
                    case "2":
                        Twodim_arr = []
                        arr_rows = int(input("Enter number of rows: "))
                        if(arr_rows < 1):
                            print("[Error: Number of rows can't be less than 1]")
                            break
                        arr_cols = int(input("Enter number of columns: "))
                        if(arr_cols < 1):
                            print("[Error: Number of columns can't be less than 1]")
                            break
                        nElements = arr_rows*arr_cols
                        elements = input(f"Enter {nElements} elements for the array separated by space: ")
                        if(len(elements.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(elements.split()) > nElements):
                            print(f"[Error: Number of elements can't be greater than {nElements}]")
                            break                        
                        transfer = elements.split(" ")
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        final_arr = transfer.copy()
                        transfer.clear()                
                        da = DataAnalytics(final_arr, arr_cols, arr_rows)
                        da.slindex(2)
                    case "3":
                        Threedim_arr = []
                        transfer = []
                        arr_rows = int(input("Enter number of rows: "))
                        if(arr_rows < 1):
                            print("[Error: Number of rows can't be less than 1]")
                            break                        
                        arr_cols = int(input("Enter number of columns: "))
                        if(arr_cols < 1):
                            print("[Error: Number of columns can't be less than 1]")
                            break
                        in_arr_rows = int(input("Enter number of in-array rows: "))
                        if(in_arr_rows < 1):
                            print("[Error: Number of in-array rows can't be less than 1]")
                            break
                        nElements = arr_cols*arr_rows*in_arr_rows
                        elements = input(f"Enter {nElements} elements for the array separated by space: ")
                        if(len(elements.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(elements.split()) > nElements):
                            print(f"[Error: Number of elements can't be greater than {nElements}]")
                            break
                        transfer = elements.split(" ")
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        final_arr = transfer.copy()
                        transfer.clear()
                        da = DataAnalytics(final_arr, arr_rows, in_arr_rows, arr_cols)
                        da.slindex(3)
                    case "4":
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "2":
            while True:
                print("\nChoose a mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Back to main menu")
                math_choice = input("Enter your choice: ")
                match math_choice:
                    case "1":
                        add_arr = []
                        add_elems = input(f"Enter {nElements} elements: ")
                        if(len(add_elems.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(add_elems.split()) > nElements):
                            print(f"[Error: Number of elements can't be greate than {nElements}")
                            break
                        transfer = add_elems.split()
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        add_arr = transfer.copy()
                        transfer.clear()
                        if not in_arr_rows and arr_rows > 1:
                            result = da.math_ope(final_arr, add_arr, arr_rows, arr_cols, math_choice)
                        elif arr_rows == 1:
                            result = da.math_ope(final_arr, add_arr, 1, arr_cols, math_choice)
                        else:
                            result = da.math_ope(final_arr, add_arr, arr_rows, arr_cols, math_choice, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSecond Array:")
                        add_arr = np.array(add_arr)
                        if not in_arr_rows and arr_rows > 1:
                            add_arr = add_arr.reshape(arr_rows, arr_cols)
                        elif arr_rows == 1:
                            add_arr = add_arr.reshape(1, arr_cols)
                        else:
                            add_arr = add_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print(add_arr)
                        print("\nResult Array:")
                        print(result)
                    case "2":
                        sub_arr = []
                        sub_elems = input(f"Enter {nElements} elements: ")
                        if(len(sub_elems.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(sub_elems.split()) > nElements):
                            print(f"[Error: Number of elements can't be greate than {nElements}")
                            break
                        transfer = sub_elems.split()
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        sub_arr = transfer.copy()
                        transfer.clear()
                        if not in_arr_rows and arr_rows > 1:
                            result = da.math_ope(final_arr, sub_arr, arr_rows, arr_cols, math_choice)
                        elif arr_rows == 1:
                            result = da.math_ope(final_arr, sub_arr, 1, arr_cols, math_choice)                            
                        else:
                            result = da.math_ope(final_arr, sub_arr, arr_rows, arr_cols, math_choice, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSecond Array:")
                        sub_arr = np.array(sub_arr)
                        if not in_arr_rows and arr_rows > 1:
                            sub_arr = sub_arr.reshape(arr_rows, arr_cols)
                        elif arr_rows == 1:
                            mul_arr = mul_arr.reshape(1, arr_cols)                            
                        else:
                            sub_arr = sub_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print(sub_arr)
                        print("\nResult Array:")
                        print(result)
                    case "3":
                        mul_arr = []
                        mul_elems = input(f"Enter {nElements} elements: ")
                        if(len(mul_elems.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(mul_elems.split()) > nElements):
                            print(f"[Error: Number of elements can't be greate than {nElements}")
                            break
                        transfer = mul_elems.split()
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        mul_arr = transfer.copy()
                        transfer.clear()
                        if not in_arr_rows and arr_rows > 1:
                            result = da.math_ope(final_arr, mul_arr, arr_rows, arr_cols, math_choice)
                        elif arr_rows == 1:
                            result = da.math_ope(final_arr, mul_arr, 1, arr_cols, math_choice)                            
                        else:
                            result = da.math_ope(final_arr, mul_arr, arr_rows, arr_cols, math_choice, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSecond Array:")
                        mul_arr = np.array(mul_arr)
                        if not in_arr_rows and arr_rows > 1:
                            mul_arr = mul_arr.reshape(arr_rows, arr_cols)
                        elif arr_rows == 1:
                            mul_arr = mul_arr.reshape(1, arr_cols)
                        else:
                            mul_arr = mul_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print(mul_arr)
                        print("\nResult Array:")
                        print(result)
                    case "4":
                        div_arr = []
                        div_elems = input(f"Enter {nElements} elements: ")
                        if(len(div_elems.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(div_elems.split()) > nElements):
                            print(f"[Error: Number of elements can't be greate than {nElements}")
                            break
                        transfer = div_elems.split()
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        div_arr = transfer.copy()
                        transfer.clear()
                        if not in_arr_rows and arr_rows > 1:
                            result = da.math_ope(final_arr, div_arr, arr_rows, arr_cols, math_choice)
                        elif arr_rows == 1:
                            result = da.math_ope(final_arr, mul_arr, 1, arr_cols, math_choice)                            
                        else:
                            result = da.math_ope(final_arr, div_arr, arr_rows, arr_cols, math_choice, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSecond Array:")
                        div_arr = np.array(div_arr)
                        if not in_arr_rows and arr_rows > 1:
                            div_arr = div_arr.reshape(arr_rows, arr_cols)
                        elif arr_rows == 1:
                            mul_arr = mul_arr.reshape(1, arr_cols)                            
                        else:
                            div_arr = div_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print(div_arr)
                        print("\nResult Array:")
                        print(result)
                    case "5":
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "3":
            while True:
                print("\nChoose an option:")
                print("1. Combine Arrays")
                print("2. Split Array")
                print("3. Back to main menu")
                comlit_choice = input("Enter your choice: ")
                match comlit_choice:
                    case "1":
                        comb_arr = []
                        comb_elems = input(f"Enter {nElements} elements: ")
                        if(len(comb_elems.split()) < nElements):
                            print(f"[Error: Number of elements can't be less than {nElements}]")
                            break
                        elif(len(comb_elems.split()) > nElements):
                            print(f"[Error: Number of elements can't be greater than {nElements}]")
                        transfer = comb_elems.split(" ")
                        for i,k in enumerate(transfer):
                            transfer[i] = int(k)
                        comb_arr = transfer.copy()
                        transfer.clear()
                        if not in_arr_rows  and arr_rows > 1:
                            result = da.combine(comb_arr, final_arr, arr_rows, arr_cols)
                        elif arr_rows == 1:
                            result = da.combine(comb_arr, final_arr, 1, arr_cols)                            
                        else:
                            result = da.combine(comb_arr, final_arr, arr_rows, arr_cols, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSecond Array:")
                        comb_arr = np.array(comb_arr)
                        if not in_arr_rows and arr_rows > 1:
                            comb_arr = comb_arr.reshape(arr_rows, arr_cols)
                        elif arr_rows == 1:
                            comb_arr = comb_arr.reshape(1, arr_cols)                            
                        else:
                            comb_arr = comb_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print(comb_arr)
                        print("\nCombined Array (Vertical Stack):")
                        print(result)
                    case "2":
                        if not arr_rows:
                            print("[Error: You need atleast 2D array for this action]")
                            break
                        split_arr = []
                        split_arr = done_arr.copy()
                        split_arr = np.array(split_arr)
                        if not in_arr_rows:
                            result = da.split(split_arr, arr_rows, arr_cols)
                        else:
                            result = da.split(split_arr, arr_rows, arr_cols, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)                    
                        print("\nSplitted Array (Horizontal Split):")
                        print(result)
                    case "3":
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "4":
            while True:
                print("\nChoose an option:")
                print("1. Search a value")
                print("2. Sort the array")
                print("3. Filter values")
                print("4. Back to main menu")
                ssf_choice = input("Enter your choice: ")
                match ssf_choice:
                    case "1":
                        value = int(input("Enter value to find:"))
                        index = np.where(done_arr == value)
                        if value not in done_arr:
                            print(f"[Error: Value {value} doesn't exist]")
                        else:
                            print("\nArray:")
                            print(done_arr)
                            print(f"\nValue {value} found at index:")
                            print(index)
                    case "2":
                        sort_arr = done_arr.copy()
                        sort_arr = np.sort(sort_arr, axis = None)
                        if not in_arr_rows:
                            sort_arr = sort_arr.reshape(arr_rows, arr_cols)
                        else:
                            sort_arr = sort_arr.reshape(arr_rows, arr_cols, in_arr_rows)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSorted Array:")
                        print(sort_arr)
                        print("(Sorting applied row-wise.)")
                    case "3":
                        filter_arr = []
                        threshold_arr = done_arr.copy()
                        while True:
                            print("\nChoose a filter:")
                            print("1. Greater than threshold")
                            print("2. Less than threshold")
                            print("3. Equals to threshold")
                            print("4. Greater than equals to threshold")
                            print("5. Less than equals to threshold")
                            print("6. Not equals to threshold")
                            print("7. Back to main menu")
                            filter_choice = input("Enter filter number: ")
                            match filter_choice:
                                case "1":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr > threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)
                                case "2":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr < threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)                                    
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)
                                case "3":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr == threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)                                    
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)
                                case "4":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr >= threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)                                    
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)
                                case "5":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr <= threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)                                    
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)
                                case "6":
                                    threshold = int(input("Enter a threshold value:"))
                                    filter_arr = threshold_arr[threshold_arr != threshold]
                                    print("\nOriginal Array:")
                                    print(done_arr)                                    
                                    print(f"Values greater than {threshold}:")
                                    print(filter_arr)                                                                                                                                                                                    
                                case "7":
                                    break
                                case _:
                                    print("Invalid choice")
                                    continue
                    case "4":
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "5":
            while True:
                print("\nChoose an aggregate/statistical operation:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
                print("6. Back to main menu")
                agg_choice = input("Enter your choice: ")
                match agg_choice:
                    case "1":
                        sum = np.sum(done_arr)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nSum of array elements:")
                        print(sum)
                    case "2":
                        mean = np.mean(done_arr)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nMean of array elements:")
                        print(mean)
                    case "3":
                        median = np.median(done_arr)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nMedian of array elements:")                        
                        print(median)
                    case "4":
                        std = np.std(done_arr)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nStandard deviation of array elements:")                        
                        print(std)
                    case "5":
                        var = np.var(done_arr)
                        print("\nOriginal Array:")
                        print(done_arr)
                        print("\nVariance of array elements:")                        
                        print(var)
                    case "6":
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        case _:
            print("Invalid Option!")
            continue