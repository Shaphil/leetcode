def reverseWords(s):
    x = s.split()
    for i in range(len(x)):
        x[i] = x[i][::-1]
    
    rev = ' '.join(x)
    return rev


if __name__ == "__main__":
    sentence = "Let's take LeetCode contest"
    rev = reverseWords(sentence)
    print(rev)
