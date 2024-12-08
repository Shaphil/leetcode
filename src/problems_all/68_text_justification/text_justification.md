# 68. Text Justification

**Difficulty -** Hard
**Topics -** `Array`, `String`, `Simulation`

## Problem Statement

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth`
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra
spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

### Note

* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
* The input array words contains at least one word.

### Example

**Input**

```javascript
words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
```

**Output**

```javascript
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

* **Link -** <https://leetcode.com/problems/text-justification/description/>

## Approach

### Understand the Problem

The goal is to format a list of words into lines that satisfy:

1. Each line has a width of exactly `maxWidth` characters.
2. Words must fit in the same order as in the input list.
3. Spaces should be distributed evenly in fully justified lines.
4. For the last line, words are left-aligned and padded with spaces to reach `maxWidth`.

### Identify the Sub-problems

To solve the problem, you need to handle three main tasks:

1. Group words into lines: Decide how many words can fit in each line without exceeding `maxWidth`.
2. Format each line:
    * For fully justified lines, distribute spaces evenly between words.
    * For the last line, left-align the words and pad with spaces at the end.
3. Combine the results: Assemble all formatted lines into a single output list.

### Strategy

#### Step 1: Group Words into Lines

* Start with the first word and add words to the current line until adding another word would exceed `maxWidth`.
* Keep track of the current line’s length (`current_length`) as the sum of the word lengths plus the number of spaces
  needed.
* Once the current line is full, move to the next line.

#### Step 2: Format Fully Justified Lines

* Calculate the number of spaces to distribute:
    * Total spaces = `maxWidth - total_word_length`.
    * If there’s more than one word in the line:
        * Divide the spaces evenly between words.
        * Distribute extra spaces to the leftmost gaps (if spaces can’t be distributed evenly).
    * If there’s only one word, pad spaces to the right to reach `maxWidth`.

#### Step 3: Format the Last Line

* Left-align all words with a single space between them.
* Add extra spaces at the end of the line to make its length `maxWidth`.

### Algorithm

1. Iterate through the words:
    * Group them into lines as described in Step 1.
2. Format each line:
    * Use space distribution logic for fully justified lines.
    * Apply left-alignment rules for the last line.
3. Output the result.

### Key Insights

* You only process the words once to group them into lines and format each line, which means the approach is
  efficient (𝑂(𝑛), where n is the total number of characters in `words`).
* Pay close attention to edge cases:
    * Lines with only one word.
    * The last line (different formatting rules).
    * Extremely short or long words.

## Example Walkthrough

**Input**

```javascript
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

### Step 1: Group Words

* Line 1: `["This", "is", "an"]` → Length: 4 + 2 + 2 + 2 (spaces) = 10
* Line 2: `["example", "of", "text"]` → Length: 7 + 2 + 4 + 2 (spaces) = 15
* Line 3: `["justification."]` → Length: 14

### Step 2: Format Fully Justified Lines

* Line 1: `"This is an"` (7 spaces distributed: 3 and 4).
* Line 2: `"example of text"` (1 space distributed to the first gap).

### Step 3: Format the Last Line

* Line 3: `"justification. "` (left-aligned, padded with spaces at the end).

**Output**

```javascript
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

## Solution

This is a solution to the problem in Python,

```python
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # To store the justified lines
        current_line = []  # To store words for the current line
        current_length = 0  # Current total length of words in the line (excluding spaces)

        for word in words:
            # Check if adding the next word exceeds maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Time to justify the current line
                for i in range(maxWidth - current_length):  # Distribute spaces
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                result.append("".join(current_line))  # Combine words and spaces
                current_line = []  # Reset for the next line
                current_length = 0

            # Add the current word to the line
            current_line.append(word)
            current_length += len(word)

        # Handle the last line (left-aligned, spaces at the end)
        result.append(" ".join(current_line).ljust(maxWidth))

        return result


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    output = Solution().fullJustify(words, maxWidth)
    print(output)
```

### Explanation

1. Key Variables:
    * `current_line`: Stores the words for the current line.
    * `current_length`: Tracks the total length of words in the current line (excluding spaces).

2. Logic:
    * For each word in words:
        * Check if adding the word to the current line exceeds maxWidth.
        * If it does, justify the current line:
            * Distribute spaces evenly between words in current_line.
            * Append the justified line to result.
        * Add the current word to the next line.
    * Finally, handle the last line separately:
        * Left-align the words and pad with spaces to the right.

3. Space Distribution:
    * `i % (len(current_line) - 1 or 1)` ensures spaces are distributed cyclically between gaps, prioritizing leftmost
      gaps. The `or 1` handles the edge case of a single word in the line.

4. Final Left Alignment:
    * The last line is simply left-aligned and padded to `maxWidth` using `ljust`.

### Complexity

**Time Complexity:** O(n), where n is the total number of characters in words. We iterate through the list once and
perform minimal additional work per word.
**Space Complexity:** O(n), for storing the result.

### Example Run

**Input**

```javascript
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

**Output**

```javascript
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

## Problem Category

The solution to this problem primarily falls under the Simulation category because it directly involves mimicking the
behavior of text formatting systems, such as justifying lines to meet a specific width while adhering to rules.

However, it also heavily incorporates elements of Arrays and Strings:

### Topics Involved in the Solution

1. Simulation
    * The problem requires step-by-step simulation of how text is justified, including word grouping, space
      distribution, and alignment. You follow a set of precise rules to "simulate" how a text editor might perform
      justification.
2. Array Manipulation
    * Words are processed as an array, and you repeatedly group them into sub-arrays (lines). Managing indices,
      distributing spaces cyclically, and reassembling words into strings all involve array manipulation.
3. String Manipulation:
    * The solution includes constructing justified strings by adding spaces and aligning words. This involves
      understanding string lengths, padding, and efficient string concatenation.
4. Greedy Algorithm (implicitly):
    * At each step, you greedily fill the current line with as many words as possible without exceeding `maxWidth`. This
      ensures that space distribution and alignment for the current line are handled optimally before moving on to the
      next line.

### Primary Topic

If asked to pick one primary topic, the solution would most closely align with Simulation, since the core task is
simulating the behavior of text justification systems while adhering to specific rules.