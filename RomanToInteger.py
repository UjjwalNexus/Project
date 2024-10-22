class Solution1:
    def romanToInt(self , s: str) -> int:
        roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10, 
        'L': 50,
        'C': 100,
        'D': 500, 
        'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i - 1]]:
                total += roman_to_int[s[i]] - 2 * roman_to_int[s[i - 1]]
            else:
                total += roman_to_int[s[i]]
        return total


print(Solution1().romanToInt("MCMXCIV"))