def unique(words):
    morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.",
            "--.-",".-.","...","-","..-","...-",".--","-..-",
            "-.--","--.."
    ]
    unique_morse = set()
    for word in words:
        word_morse = ''
        for letter in word:
            word_morse += morse[ord(letter.lower()) - ord('a')]
        
        unique_morse.add(word_morse)
    
    return len(unique_morse)


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    morses = unique(words)
    print(morses)

