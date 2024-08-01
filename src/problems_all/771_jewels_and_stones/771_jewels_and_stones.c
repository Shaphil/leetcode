#include <stdio.h>
#include <string.h>

int numJewelsInStones(char *J, char *S) {
  int a = strlen(J);
  int b = strlen(S);
  int count = 0;

  for (int i = 0; i < a; i++)
    for (int j = 0; j < b; j++)
      if (J[i] == S[j])
        count++;

  return count;
}

int main() {
  char *jewels = "aA";
  char *stones = "aAAbbbb";

  int count = numJewelsInStones(jewels, stones);
  printf("count: %d\n", count);
}