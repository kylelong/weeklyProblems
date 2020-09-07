public class compress {
    public static void main(String[] args) {
        char[] chars = { 'a', 'a', 'b', 'b', 'b', 'c', 'c' };
        chars = compresser(chars);
        for (char c : chars) {
            System.out.print(c + " ");
        }
    }

    public static char[] compresser(char[] chars) {
        int i = 0; // less than chars.length
        int index = 0; // length of new array
        while (i < chars.length) {
            char c = chars[i];
            int count = 0;
            while (i < chars.length && chars[i] == c) {
                i++;
                count++;
            }
            chars[index++] = c;
            if (count != 1) {
                for (char s : String.valueOf(count).toCharArray()) {
                    chars[index++] = s;
                }
            }
        }
        return chars;

    }
}