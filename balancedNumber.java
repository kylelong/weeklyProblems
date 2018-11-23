/**
 * Created by kylel95 on 11/22/18.
 */
import java.util.*;
public class balancedNumber {
//    Write a function to determine if the frequency of digits in a given number is balanced.
    public static void main (String [] args){
   System.out.println(freq(1337));
   System.out.println(freq(3.1415926535));
   System.out.println(freq(12345678));

    }

    /**
     * Checks the frequency of each digit in a number
     * Determines if each digit occurs the same, which would make the
     * number balanced.
     * @param d the number to determine if it is balanced
     * @return whether the number is balanced or not
     */
    public static boolean freq(double d){
        String s = String.valueOf(d);
        HashMap<Character, Integer> map = new HashMap<>();
        //ignore the .0 at the end since its a string from a double
        char c = ' ';
        //map digit to its occurrence
        for(int i = 0; i < s.length() - 2; i++){
             c = s.charAt(i);
            if(!map.containsKey(c)){
                map.put(c, 1);
            }
            else{
                map.put(c, map.get(c) + 1);
            }
        }
        int [] arr = new int[map.size()];
        int k = 0;
        for(char ch: map.keySet()){
            arr[k] = map.get(ch);
            k++;
        }
        Arrays.sort(arr);
        //if arrays indices are not equal, string is not balanced.
        return arr[0] == arr[arr.length - 1];
    }
}
