
//package com.company;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * https://open.kattis.com/problems/piglatin Converts a string to pig latin
 * Created by Kyle Long on 11/3/2016.
 */
public class piglatin {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String alpha = "aeiouy";

        // while(scan.hasNextLine())
        // {
        // String s = scan.nextLine();
        // System.out.println(pig(s));
        // }
        System.out.println(pig("i cant speak pig latin")); // iyay antcay eakspay igpay atinlay
        /**
         * ethay uickqay ownbray oxfay umpsjay overyay ethay azylay ogday andyay
         * ordinaryyay oxesfay ontday umpjay overyay azylay ogsday
         */
        System.out.println(
                pig("the quick brown fox jumps over the lazy dog and ordinary foxes dont jump over lazy dogs"));

    }

    /**
     * Converts a string to pig latin If a word begins with a consonant, take all of
     * the letters before the first vowel and move them to the end of the word, then
     * add ay to the end of the word. Examples: pig → igpay, there → erethay.
     * 
     * If a word begins with a vowel (a, e, i, o, u, or y), simply add yay to the
     * end of the word. For this problem, y is always a vowel. Examples: and →
     * andyay, ordinary → ordinaryyay.
     * 
     * @param s The line to be converted to pig latin
     * @return The pig latin version of the string
     */
    public static String pig(String s) {
        String alpha = "aeiouy";
        StringBuilder sb = new StringBuilder();
        ArrayList<String> list = new ArrayList<>();
        for (String phrase : s.split(" ")) {
            list.add(phrase);
        }
        for (int i = 0; i < list.size(); i++) {
            String curr = list.get(i);
            if (alpha.contains(String.valueOf(curr.charAt(0)))) {
                sb.append(curr + "yay ");
            } else if (!alpha.contains(String.valueOf(curr.charAt(0)))) {
                String prefix = curr.substring(0, index(curr));
                sb.append(curr.substring(index(curr), curr.length()) + prefix + "ay ");
            }
        }
        return sb.toString();
    }

    /**
     * If the word in a string does not begin with a vowel the first index of the
     * vowel is returned so a new string with everything before the first vowel is
     * appended to the end of the string
     * 
     * @param s The string to be passed in
     * @return The index of the first vowel
     */
    public static int index(String s) {
        String alpha = "aeiouy";
        int count = 0;
        for (int i = 0; i < alpha.length(); i++) {
            String c = String.valueOf(s.charAt(i));
            if (!alpha.contains(c)) {
                count++;
            } else {
                break;
            }
        }
        return count;
    }
}
