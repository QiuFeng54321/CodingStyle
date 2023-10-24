# is anagram
def is_Anagram(a,b):
    if len(a)==len(b):
      v=[False]*len(a)
      for I in range(len(a)):
        f=False
        for J in range(len(b)):
            if not v[J]:
              if b[J]==a[I]:
                  v[J]= True
                  f =True
                  break
        if not f:return False
      return True
    else:
      return False

print(is_Anagram("earth", "heart"))
print(is_Anagram("earth", "herrt"))
print(is_Anagram("earth", "heartt"))