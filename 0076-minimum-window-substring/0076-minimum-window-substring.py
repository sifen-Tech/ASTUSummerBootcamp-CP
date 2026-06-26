class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_counter = defaultdict(int)
        for char in t:
            char_counter[char] += 1

        min_window = (0, float("inf"))
        # the number of remaining required characters
        target = len(t)
        left = 0

        for right in range(len(s)):
            if char_counter[s[right]] > 0:
                target -= 1
            char_counter[s[right]] -= 1

            # found a substring with all characters from t
            if target == 0:
                while True:
                    if char_counter[s[left]] == 0:
                        break
                    char_counter[s[left]] += 1
                    left += 1

                if right-left < min_window[1] - min_window[0]:
                    min_window = (left, right)

                # s[left] in t -> recalculate the counters
                char_counter[s[left]] += 1
                target += 1
                left += 1

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]