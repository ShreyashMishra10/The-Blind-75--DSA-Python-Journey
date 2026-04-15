class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_str = ""
        k = 0
        for char in s:
            if char.isdigit():
                k= k * 10 + int(char)
            elif char == '[':
                count_stack.append(k)
                string_stack.append(current_str)
                current_str = ""
                k = 0
            elif char == ']':
                repeat_times = count_stack.pop()
                last_str = string_stack.pop()
                current_str = last_str + (repeat_times * current_str)
            else:
                current_str += char
        return current_str