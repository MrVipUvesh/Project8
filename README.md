# NumPy Analyzer

NumPy Analyzer is a menu-driven Python application designed to create, manipulate, and analyze multidimensional arrays using NumPy. It provides a collection of operations for array indexing, slicing, arithmetic calculations, combining and splitting arrays, searching, sorting, filtering, and statistical analysis.

The project brings together several NumPy features in one interactive program and provides practical experience with array manipulation, numerical computations, and structured Python programming.

## Features

### 1. Array Creation
Create arrays of different dimensions by entering the required dimensions and elements.

- Create 1D arrays.
- Create 2D arrays with specified rows and columns.
- Create 3D arrays with specified rows, columns, and in-array dimensions.
- Validate the number of elements entered.
- Display the created array.

### 2. Indexing and Slicing
Access individual elements or select portions of an array.

- Retrieve an element using its index.
- Slice a 1D array using start and end indices.
- Access elements in a 2D array using row and column indices.
- Slice a 2D array by specifying row and column ranges.

### 3. Mathematical Operations
Perform element-wise arithmetic operations between arrays of compatible shapes.

- Addition
- Subtraction
- Multiplication
- Division

The program accepts a second set of values, arranges them into the appropriate shape, and displays the original array, second array, and resulting array.

### 4. Combine and Split Arrays
Manipulate arrays by joining or dividing their contents.

- Combine two arrays using vertical stacking.
- Split an array into two sections.
- Display the original arrays and the resulting arrays.
- Check whether the row count is suitable for splitting.

### 5. Search, Sort, and Filter
Perform common data-processing operations on an existing array.

**Search**
- Search for a specified value.
- Display the indices where the value occurs.
- Display an error message when the value is not found.

**Sort**
- Sort array elements in ascending order.
- Preserve the original array by working on a copy.
- Reshape the sorted data to its original dimensions.

**Filter**
- Greater than a threshold
- Less than a threshold
- Equal to a threshold
- Greater than or equal to a threshold
- Less than or equal to a threshold
- Not equal to a threshold

Each filtering operation displays the original array and the selected values.

### 6. Aggregates and Statistical Analysis
Calculate numerical summaries of the array using NumPy.

- Sum
- Mean
- Median
- Standard deviation
- Variance

The original array and the calculated result are displayed for each operation.

## Technologies Used

- Python 3.10 or later
- NumPy
- Classes and objects
- Functions and methods
- Lists and arrays
- Loops and conditional statements
- `match-case` statements
- User input and output
- Type conversion
- Array reshaping
- Array indexing and slicing
- Element-wise arithmetic
- NumPy statistical functions

## Requirements

- Python 3.10 or later
- NumPy

Install NumPy using pip:

    python -m pip install numpy

If your system uses `python3`, you can also run:

    python3 -m pip install numpy

## Project Structure

    Numpy-Analyzer/
    ├── main.py
    └── README.md

The `main.py` file contains the `DataAnalytics` class and the menu-driven application.

## How to Run

1. Install Python and NumPy.
2. Save the program in a Python file, such as `main.py`.
3. Open a terminal or command prompt in the project directory.
4. Execute the following command:

       python main.py

The program displays the main menu and allows you to choose an operation.

## Main Menu

The application provides the following options:

    Welcome to the Numpy Analyzer!

    Choose an option:
    1. Create a Numpy Array
    2. Perform Mathematical Operations
    3. Combine or Split Arrays
    4. Search, Sort, or Filter Arrays
    5. Compute Aggregates and Statistics
    6. Exit

Each option opens a dedicated submenu where the corresponding operations can be performed.

## Usage Examples

The following examples demonstrate the program's intended functionality. The outputs are illustrative and may vary depending on the input.

### 1. Creating a 1D Array

Select option `1` and then choose `1D Array`.

    Enter number of elements: 5
    Enter 5 elements for the array separated by space: 10 20 30 40 50

    Array created successfully:
    [10 20 30 40 50]

A 1D array stores its elements along a single axis.

### 2. Creating a 2D Array

Choose `2D Array` and enter the number of rows, columns, and elements.

    Enter number of rows: 2
    Enter number of columns: 3
    Enter 6 elements for the array separated by space: 10 20 30 40 50 60

    Array created successfully:
    [[10 20 30]
     [40 50 60]]

The entered elements are reshaped into two rows and three columns.

### 3. Creating a 3D Array

Choose `3D Array` and provide the required dimensions.

For example, two rows, three columns, and two in-array rows require 12 elements.

    Enter number of rows: 2
    Enter number of columns: 3
    Enter number of in-array rows: 2
    Enter 12 elements for the array separated by space: 1 2 3 4 5 6 7 8 9 10 11 12

The program arranges the elements into a three-dimensional NumPy array according to the dimensions supplied.

### 4. Indexing and Slicing

For a 1D array:

    [10 20 30 40 50]

To access the element at index `2`:

    Enter index number: 2

    Element at index you choosed:
    30

Python uses zero-based indexing, so index `2` refers to the third element.

To slice the same array:

    Enter starting index: 1
    Enter ending index: 4

    Sliced Array:
    [20 30 40]

The ending index is excluded from the slice.

For a 2D array, indexing requires both a row index and a column index. Slicing allows a range of rows and columns to be selected.

### 5. Mathematical Operations

Suppose the original array is:

    [[10 20 30]
     [40 50 60]]

For addition, enter another set of six elements:

    Enter 6 elements: 1 2 3 4 5 6

The result is:

    Result Array:
    [[11 22 33]
     [44 55 66]]

The same process can be used for subtraction, multiplication, and division.

These operations are performed element by element using NumPy functions.

### 6. Combining Arrays

The combine operation uses vertical stacking to join two arrays.

For example:

    Original Array:
    [[1 2]
     [3 4]]

    Second Array:
    [[5 6]
     [7 8]]

    Combined Array (Vertical Stack):
    [[5 6]
     [7 8]
     [1 2]
     [3 4]]

The output order reflects the order in which the arrays are passed to the stacking function.

### 7. Splitting an Array

The split operation divides an array into two sections along its rows.

For an array with four rows:

    [[1 2]
     [3 4]
     [5 6]
     [7 8]]

The result contains two arrays:

    [[1 2]
     [3 4]]

    [[5 6]
     [7 8]]

The implementation requires an even number of rows for this operation.

### 8. Searching for a Value

Suppose the array is:

    [[10 20 30]
     [40 20 60]]

Enter the value to search for:

    Enter value to find: 20

The program uses `np.where()` to identify the positions where the value occurs.

Because the value appears twice, the returned indices identify both matching positions.

### 9. Sorting an Array

The sorting operation arranges array elements in ascending order.

For example:

    Original Array:
    [[30 10 20]
     [60 40 50]]

    Sorted Array:
    [[10 20 30]
     [40 50 60]]

The implementation sorts the flattened values and reshapes the result to match the original dimensions. Therefore, the elements are sorted globally before being placed back into the array's shape.

### 10. Filtering Array Values

Filtering selects elements based on a comparison with a threshold.

For example, given:

    Original Array:
    [10 20 30 40 50]

If the selected operation is greater than or equal to the threshold and the threshold is `30`, the result is:

    Values greater than or equal to 30:
    [30 40 50]

The program supports six comparison conditions, allowing different subsets of the array to be extracted.

### 11. Calculating the Sum

Given the array:

    [10 20 30 40 50]

The sum operation uses `np.sum()`.

    Sum of array elements:
    150

### 12. Calculating the Mean

The mean is calculated using `np.mean()`.

    Mean of array elements:
    30.0

It represents the arithmetic average of the array elements.

### 13. Calculating the Median

The median is calculated using `np.median()`.

For the array:

    [10 20 30 40 50]

The output is:

    Median of array elements:
    30.0

The median represents the middle value after the values are ordered.

### 14. Calculating Standard Deviation

The standard deviation is calculated using `np.std()`.

For the array:

    [10 20 30 40 50]

The population standard deviation is approximately:

    14.1421

NumPy uses population standard deviation by default with `np.std()`.

### 15. Calculating Variance

The variance is calculated using `np.var()`.

For the array:

    [10 20 30 40 50]

The population variance is:

    200.0

NumPy uses population variance by default with `np.var()`.

## Class Overview

### `DataAnalytics`

The `DataAnalytics` class contains the methods used to manipulate and analyze arrays.

**`__init__(self, elems, cols, rows=1, dim=0)`**

Creates a NumPy array from the supplied elements and reshapes it according to the selected dimensions.

**`slindex(self, arrType)`**

Provides indexing and slicing options. The `arrType` argument determines which indexing and slicing interface is displayed.

**`math_ope(self, arr1, arr2, row, col, operation, dim=0)`**

Performs addition, subtraction, multiplication, or division on two arrays and reshapes the result according to the supplied dimensions.

**`combine(self, arr1, arr2, row, col, dim=0)`**

Combines two arrays using `np.vstack()` and reshapes the resulting array.

**`split(self, arr, row, col, dim=0)`**

Splits an array into two sections using `np.vsplit()`, provided the number of rows is even.

## NumPy Functions Used

| Function | Purpose |
|---|---|
| `np.array()` | Creates a NumPy array. |
| `reshape()` | Changes the dimensions of an array. |
| `np.add()` | Adds corresponding elements. |
| `np.subtract()` | Subtracts corresponding elements. |
| `np.multiply()` | Multiplies corresponding elements. |
| `np.divide()` | Divides corresponding elements. |
| `np.vstack()` | Stacks arrays vertically. |
| `np.vsplit()` | Splits an array vertically. |
| `np.where()` | Finds positions satisfying a condition. |
| `np.sort()` | Sorts array elements. |
| `np.sum()` | Calculates the sum. |
| `np.mean()` | Calculates the mean. |
| `np.median()` | Calculates the median. |
| `np.std()` | Calculates the standard deviation. |
| `np.var()` | Calculates the variance. |

## Important Notes

- Enter integer values separated by spaces when creating arrays.
- The number of elements must match the specified dimensions.
- Indexing starts at zero.
- The ending index in a slice is excluded.
- Mathematical operations require compatible array shapes.
- Division by zero should be avoided when performing array division.
- The split operation requires an even number of rows.
- The program uses shared variables to track the current array and its dimensions. Operations should be performed after creating an array.
- NumPy's default `np.std()` and `np.var()` calculate population statistics.
- The program is intended as a learning project; additional validation may be needed to handle every invalid input safely.

## Learning Objectives

This project provides practical experience with:

- Creating and reshaping multidimensional arrays
- Understanding array dimensions and indexing
- Extracting data through slicing
- Performing element-wise mathematical operations
- Combining and splitting arrays
- Searching and sorting numerical data
- Applying conditional filters
- Calculating descriptive statistics
- Using NumPy functions in an interactive program
- Organizing functionality through classes and methods
- Building nested menus using loops and conditional statements

## Conclusion

NumPy Analyzer brings together core array operations and statistical calculations in a single command-line application. It demonstrates how NumPy can simplify numerical processing while providing a practical environment for learning multidimensional arrays, data manipulation, and basic statistical analysis.

The project can be extended with additional functionality, including more robust input validation, support for floating-point values, matrix operations, and more advanced data analysis tools.

## Author
- Uvesh Ansari
