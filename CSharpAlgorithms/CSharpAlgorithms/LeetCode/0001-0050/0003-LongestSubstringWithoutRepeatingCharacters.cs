// https://leetcode.com/problems/longest-substring-without-repeating-characters/

using System.Collections.Generic;

namespace LeetCode
{
    public class _0003_LongestSubstringWithoutRepeatingCharacters
    {
        public int LengthOfLongestSubstring(string s)
        {
            if (string.IsNullOrEmpty(s)) return 0;

            var dict = new Dictionary<int, int>();
            int maxLength = 0;
            int lastRepeatPos = -1;

            for (int i = 0; i < s.Length; i++)
            {
                if (dict.ContainsKey(s[i]) && lastRepeatPos < dict[s[i]] )
                    lastRepeatPos = dict[s[i]];
                if (maxLength < i - lastRepeatPos)
                    maxLength = i - lastRepeatPos;
                dict[s[i]] = i;
            }

            return maxLength;
        }
    }
}