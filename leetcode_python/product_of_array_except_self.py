'''
{              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
{ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        output = [1]
        for x in nums[:-1]:
            output.append(x * output[-1])

        running_product = 1
        for i in range(len(nums) - 2, -1, -1):
            running_product *= nums[i + 1]
            print running_product
            output[i] *= running_product

        return output
