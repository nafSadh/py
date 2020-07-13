import sys

words = [
  "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
  "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
  "sixteen", "seventeen", "eighteen", "nineteen"
  ]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]  

def phrase_num(n):
  def triplets(num, mod, phrase):
    m = num%mod
    return phrase_num(int(num/mod))+' '+phrase+ (' '+phrase_num(m) if m > 0 else '')
  if n==0: return "zero" 
  if 0 < n < 20: return words[n]
  if 20<= n < 100: 
    m = n%10
    return tens[int(n/10)]+ ('-'+words[m] if m>0 else '')
  if 100<= n < 1000: 
    m = n%100
    return words[int(n/100)]+' hundred' + (' '+phrase_num(m) if m > 0 else '')
  if 1000<= n < 1000**2: return triplets(n, 1000, "thousand")
  if 1000**2<= n < 1000**3: return triplets(n, 1000**2, "million")
  if 1000**3<= n < 1000**4: return triplets(n, 1000**3, "billion")
  if 1000**4<= n < 1000**5: return triplets(n, 1000**4, "trillion")
  return triplets(n, 1000**5, "trillion")


if __name__ == '__main__':
  print(phrase_num(int(sys.argv[1])))
