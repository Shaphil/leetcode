/*
https://leetcode.com/problems/to-lower-case/description/

Runtime: 4 ms
Memory: 6.5 MB
*/

#include <stdio.h>

char *toLowerCase(char *str)
{
    for (char *c = str; *c; c++)
        if (*c >= 'A' && *c <= 'Z')
            *c = (*c - 'A') + 'a';

    return str;
}

int main()
{
    char *s = "Hello";
    char *result = toLowerCase(s);
    printf("%s\n", result);

    return 0;
}
