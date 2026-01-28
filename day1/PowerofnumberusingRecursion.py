def power(a,b,ans):
    if b==0:
        return ans
    ans=ans*a
    return power(a,b-1,ans)
a=2
b=3
ans=1
print(power(a,b,ans))