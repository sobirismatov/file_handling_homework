def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k=data.split('\n')
    a=[]
    for i in k:
        a.append(len(str(i)))
    return a
f= open('./txt_file/data06.txt')
data=f.read()
print(main(data))
# Read data from file