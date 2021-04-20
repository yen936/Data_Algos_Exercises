# Data_Algos_Exercises
Some code I wrote to complete exercises from my Data Structures and Algorithms course.  


## cartesian.py

Given a point P (p) on a cartesian plane, take a given amount of steps along the x-axis and y-axis for each iteration and get as close to p as possible. 
After every 3rd iteration, take a given amount of steps backwards in the x and y directions.
Arrive at a point (x, y) whose distance is closest to p (using the distance formula). Start at the origin (0,0).

1) Define a dynamic programming algorithm that advances and retreats the required number of steps along the x and y axes and determines the closest point to p. After each iteration, calculate the distance between point p and the current location using the distance function:
d = sqrt((x_p - x_1)^2 + (y_p - y_1)^2)
Count the number of iterations. Hint: Keep track of the previous location.

2) Output the final arrival point (the point closest to p), the distance between the arrival point and p, and the number of iterations taken.

## Binary Search Tree

BST traversal - Find keys in a range. Given 2 alphanumeric values, implement a find_in_range() function that finds all keys within the range of the 2 values that branch from a specific node's key (including the specified node).

Code to read in and insert values into the tree has been provided as well as code to print the resulting list key within the range.

1) Read in the beginning and ending values of the range. The ending value must be greater than the beginning. The values can include any ASCII character (not just integers).

2) Read in the key of the node that find_in_range() will start from and find the node in the tree.

3) Implement the find_in_range() function. find_in_range() has 3 cases to determine if the current node's key is:
    - less than the beginning range value
    - within the range
    - or greater than the ending range value

Store all keys within the range in the list keys_in_range.


