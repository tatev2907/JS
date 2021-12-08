import collections
def palindromeRearranging(inputString):
  cnt = collections.Counter()
  odds = 0
  for i in range(len(inputString)):
    cnt[inputString[i]] += 1
  for i in cnt:
    if cnt[i]%2 == 1:
      odds += 1
  return odds <= 1


print(palindromeRearranging('aabbcc'))