'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''

class Solution:
    def compress(self, chars: list[str]) -> int:
    # Initialize pointers and variables
        write = 0  # Pointer for writing the compressed result
        read = 0   # Pointer for reading the original list
        length = len(chars)  # Length of the input list
        
        # Iterate through the list until the read pointer reaches the end
        while read < length:
            char = chars[read]  # Current character to be compressed
            count = 0  # Counter for occurrences of the current character
            
            # Count the number of consecutive occurrences of the current character
            while read < length and chars[read] == char:
                read += 1  # Move the read pointer to the next character
                count += 1  # Increment the count of the current character
            
            # Write the current character to the write pointer
            chars[write] = char
            write += 1  # Move the write pointer to the next position
            
            # If the count of the current character is greater than 1,
            # write the count as individual characters
            if count > 1:
                for digit in str(count):  # Convert the count to a string and iterate over each digit
                    chars[write] = digit  # Write each digit to the write pointer
                    write += 1  # Move the write pointer to the next position
        
        # Return the length of the compressed list
        return write
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.compress(chars = ["a","a","b","b","c","c","c"]))