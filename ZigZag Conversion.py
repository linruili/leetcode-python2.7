def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
     """
    if numRows == 1:
        return s
    lines = []
    for i in range(0,numRows):
        j = i
        if j<len(s):
            lines.append(s[j])
        while j<len(s):
            j = j+2*(numRows-i-1)
            if j < len(s) and i != numRows-1:
                lines.append(s[j])
            j= j+2*i
            if j < len(s) and i != 0:
                lines.append(s[j])
    return "".join(lines)

print convert("Afsd", 1)

