import java.util.*;
public class EvenRangeSequences{
    /**
    Given an integer n, write a function to count all possible sequences of length n 
    such that all the elements of the sequence are in the range [1 to n] and the sum 
    of the elements of the sequence is even.
     */
    static ArrayList<String> list = new ArrayList<>();
    /**
     * Generates list of even range sequences
     * @param n range of sequence 1..n inclusive
     * @param str string to be permuted
     * @param arr array to be permuted
     */
    public void generate(int n, String str, char [] arr){
        if(n == arr.length){
            if(hasEvenSum(arr)){
                list.add(Arrays.toString(arr));
            }
            return;
        }
        for(int i = 0; i < str.length(); i++){
            arr[n] = str.charAt(i);
            generate(n + 1, str, arr);
        } 
    }
    /**
     * Counts even sequences of perumtations from 1..n inclusive
     * @param n range of sequences 1..n inclusive
     * @return number of even sequences
     */
    public static int countEventSequences(int n){
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <= n; i++){
            sb.append(i);
        }
        String s = sb.toString();
       new EvenRangeSequences().generate(0, s, new char[s.length()]);
       return list.size();

    }
    /**
     * Checks if a character array of integers sum is even
     * @param arr array of characters
     * @return whether the sum of the characters are even
     */
    public static boolean hasEvenSum(char [] arr){
        int sum = 0, num;
        for(char c: arr){
            num = Integer.parseInt(String.valueOf(c));
            sum += num;
        }
        return sum % 2 == 0;

    }
    public static void main(String [] args){
        int n = 3;
        System.out.println(countEventSequences(n)); //13

    }


}