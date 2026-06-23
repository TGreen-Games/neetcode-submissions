class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        text = "".join(char.lower() for char in s if char.isalnum())
        j = len(text) - 1

      
        while i < j:
            if text[i] == text[j]:
                 i += 1
                 j -= 1
            else:
                return False

        return True

        