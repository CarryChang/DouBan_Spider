import re
data = '看过(49684)'
print(re.findall(r"\d+\.?\d*",data))
