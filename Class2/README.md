## maximum subArray solving algorithm 
### Simple Approach 
## The simple approach to solve this problem is to run two for loops and for every subarray check if it is the maximum sum possible. Follow the below steps to solve the problem.

## Run a loop for i from 0 to n – 1, where n is the size of the array.
## Now, we will run a nested loop for j from i to n – 1 and add the value of the element at index j to a variable currentMax.
## Lastly, for every subarray, we will check if the currentMax is the maximum sum of all contiguous subarrays.

### Kadane's algorithm 
## Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.
## Initialize currSum with 0 and maxSum with INT_MIN.
## Now, iterate over the array and add the value of the current element to currSum and check
## If currSum is greater than maxSum, update maxSum equals to currSum.
## If currSum is less than zero, make currSum equal to zero.
## Finally, print the value of maxSum.