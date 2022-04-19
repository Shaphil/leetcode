def reverseString(s):
    _len = len(s) - 1
    it = _len // 2 + 1
    for i in range(it):
        s[i], s[_len - i] = s[_len - i], s[i]


if __name__ == "__main__":
    a = ["H","a","n","n","a","h"]
    reverseString(a)
    print(a)



# ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]