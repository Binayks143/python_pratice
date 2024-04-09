#Find E-mail id
import re
mail='abc@gmail.com abc1211@gmail.com'
print(re.findall(r'\w+\@\w+\.\w+',mail))

#E.g 2
mail='baba@yahoo.co.in'
print(re.findall(r'\w+\@\w+\.\w{2}\.\w{2}',mail))

#E.g 3 find abc@gmail.com and xyz.abc@gmail.com
mail='abc@gmail.com xyz.abc@gmail.com'
print(re.findall(r'\w+\.?\w*\@\w+\.\w+',mail))

#E.g 4 find abc@gmail.com , xyz.abc@gmail.com and xyz.abc.pqr@gmail.com
mail='abc@gmail.com xyz.abc@gmail.com xyz.abc.pqr@gmail.co'
print(re.findall(r'\w+\.?\w*\.?\w*\@\w+\.\w+',mail))

#E.g 5 find abc@gmail.com , xyz.abc@gmail.com , xyz.abc.pqr@gmail.com and xyz.abc.pqr@yahoo.co.in
mail='abc@gmail.com xyz.abc@gmail.com xyz.abc.pqr@gmail.com xyz.abc.pqr@yahoo.co.in'
print(re.findall(r'\w+\.?\w*\.?\w*\@\w+\.\w+\.?\w*',mail))
#Or
print(re.findall(r'\w+\.?\w*\.?\w*\@ [a-z A-Z]+\.?[a-zA-Z]+\.?[a-zA-Z]{2,3}\.[a-zA-Z]{1.,3}',mail))
