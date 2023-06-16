s1 = "Have a Nice Day"
s2 = "Happy Day"

print(s1.startswith("Have")) #True

print(s1.startswith("Happy")) #False

print(s1.endswith("Day")) #true

s3 = s1.replace(" ","*") #공백->별
print(s3)

print(s1.count("a")) # a갯수

print(s1.lower(),s1.upper()) # 소문자,대문자

print('/'.join(s1)) # 글자 사이 / 넣기

print(s1.isalpha()) # 모두 알파벳 = true

print(s1.isdigit()) # 모두 숫자 = true

