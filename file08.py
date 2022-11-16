def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mx=0
    for i in data:
        if mx<i:
            mx=i
    return mx
f=open('./txt_file/data08.txt')
data=f.read()
print(main(data))
# Read data from file