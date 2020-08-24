/**
 * Cassido interview problem of the week 8/23/2020
 */
public class Chars {
    public static void main(String[] args) {
        int num = numChars("oh heavens", 'h');
        System.out.println(num); // 2
    }

    /**
     * Counts how many times a character occurs in a string
     * 
     * @param str the string (haystack)
     * @param ch  the character to count for (needle)
     * @return number of times ch is in str
     */
    public static int numChars(String str, char ch) {
        int[] chars = new int[26];
        str = str.replaceAll("\\s+", ""); // remove all whitespace
        for (char c : str.toCharArray()) {
            chars[c - 'a']++;
        }
        return chars[ch - 'a'];
    }
}