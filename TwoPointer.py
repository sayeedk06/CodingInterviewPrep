class TwoPointer:
    def __init__(self, givenInput, target) -> None:
        self.target = target
        self.givenInput = givenInput
    def PairwithTargetSum(self):
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


x = list(map(int, input('Enter the given input -> ').split()))
y = int(input('Enter the target value - > '))
test = TwoPointer(x,y)

print(test.PairwithTargetSum())

    