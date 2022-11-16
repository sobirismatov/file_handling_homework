def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    k=0
    a=[]
    for i in data:
        if i.isdigit():
            k+=i
    return a.append(k)
f= open('./txt_file/data06.txt')
data=f.read()
print(main(data))

# Read data from file