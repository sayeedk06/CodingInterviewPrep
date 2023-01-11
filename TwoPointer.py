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

            

x = list(map(int, input('Enter the given input -> ').split()))
# y = int(input('Enter the target value - > '))
test = TwoPointer(x)
# print(test.PairwithTargetSum())
print(test.RemoveDuplicate())

    