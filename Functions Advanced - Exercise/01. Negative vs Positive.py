def print_negative_positive(nums):
    negative_sum = sum(filter(lambda x: x < 0, nums))
    positive_sum = sum(filter(lambda x: x > 0, nums))
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
print_negative_positive(numbers)
