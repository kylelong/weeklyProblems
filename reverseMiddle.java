/**
 * Created by kylel95 on 12/12/18.
 */
import java.util.*;
public class reverseMiddle {
    public static void main(String [] args){
        String s = "Experience is the hardest kind of teacher; it gives the test first and the lesson afterward.";
        System.out.println(reverseMid(s));
    }

    /**
     * Reverses all words in a sentence, except the first and last word.
     * @param s the string to be reversed as described above
     * @return the reversed sentence
     */
    public  static String reverseMid(String s){
        StringBuilder sb = new StringBuilder();
        String [] arr = s.split(" ");
        sb.append(arr[0] + " ");
        for(int i = 1; i <= arr.length - 2; i++){
            sb.append(reverse(arr[i]) + " ");
        }
        if(arr.length > 1){
            sb.append(arr[arr.length - 1]);
        }
        return sb.toString();
    }

    /**
     * Reverse string recursively
     * @param s string to be reverse
     * @return the reversed string
     */
    public static String reverse(String s) {
        if ((s == null) || (s.length() <= 1)) {
            return s;
        }
        return reverse(s.substring(1)) + s.charAt(0);
    }

}
