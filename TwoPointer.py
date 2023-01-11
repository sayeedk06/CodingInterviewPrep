class TwoPointer:
    def __init__(self, givenInput, target=None) -> None:
        self.target = target
        self.givenInput = givenInput
    def PairwithTargetSum(self):

        # Time Complexity = O(N)
        # Space Complexity = O(1)
        start = 0
        end = len(self.givenInput)-1
        sum = 0
        while(sum != self.target and start < end):
            sum = self.givenInput[start] + self.givenInput[end]
            if sum > self.target:
                end -= 1
            elif sum < self.target:
                start += 1
            else:
                return [start, end]
        
        return "No possible solution is present"
    
    #The next following functions are from the separating duplicates part

    def RemoveDuplicate(self):

        # Time Complexity = O(N)
        # Space Complexity = O(1)
        i = 0
        non_duplicate = 1

        while(i < len(self.givenInput)):
            if self.givenInput[non_duplicate - 1] != self.givenInput[i]:
                self.givenInput[non_duplicate] = self.givenInput[i]
                non_duplicate += 1
            i += 1
        return non_duplicate

    def RemoveKeyInstance(self, key):

        i = 0
        non_duplicate = 0

        while(i<len(self.givenInput)):
            if self.givenInput[i] != key:
                self.givenInput[non_duplicate] = self.givenInput[i]
                non_duplicate += 1
        return non_duplicate

    #The next following function is from the Squaring Sorted Array part
    def SquaringASortedArray(self):
        # [-2,-1,0,2,3]

        #Time Complexity = O(N)
        left_side, right_side = 0, len(self.givenInput) - 1
        new_array = [0 for i in range(len(self.givenInput))]
        new_array_pointer = len(self.givenInput) - 1
        
        for i in range(len(self.givenInput)):
            left_square = self.givenInput[left_side] * self.givenInput[left_side]
            right_square = self.givenInput[right_side] * self.givenInput[right_side]

            print("new_array=", new_array)
            print("left_square =", left_square)
            print("right_square =", right_square)

            if left_square > right_square:
                new_array[new_array_pointer] = left_square
                new_array_pointer -= 1
                left_side += 1
            elif right_square > left_square:
                new_array[new_array_pointer] = right_square
                new_array_pointer -= 1
                right_side -= 1
            else:
                new_array[new_array_pointer] = right_square
                new_array_pointer -= 1
                right_side -= 1

        return new_array

                


            

x = list(map(int, input('Enter the given input -> ').split()))
# y = int(input('Enter the target value - > '))
test = TwoPointer(x)
# print(test.PairwithTargetSum())
# print(test.RemoveDuplicate())
print(test.SquaringASortedArray())

    