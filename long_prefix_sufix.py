def computeLPSArray(s):
    length = 0
    lps = [0] * len(s)  # Initialize the LPS array with zeros
    i = 1

    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def lps(s):
    lps_array = computeLPSArray(s)
    return lps_array[-1]
