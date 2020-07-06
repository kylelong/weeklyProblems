import java.util.*;
public class Alternate{
	/** 
	Given string S, print the longest subsequence from S that contains alternating vowels and consonants. 
	If multiple such subsequences exist having the same length, print the subsequence with the maximum sum
	of ASCII values of its characters.
	**/
	public static void main(String [] args){
		System.out.println(alternateChars("ababab")); //ababab
		System.out.println(alternateChars("cassidyisanerd")); //casidisaner
		
	}
	/**
	Returns longest subsequence from s that contains alternating vowels and consonants.
	**/
	public static String alternateChars(String s){
		char [] v = {'a', 'e', 'i', 'o', 'u'};
		char [] c = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'};
		HashMap<Integer, List<String>> map = new HashMap<Integer, List<String>>();
		List<Character> vowels = new ArrayList<>();
		List<Character> consonants = new ArrayList<>();
		String longest = null;
		int max = 0;
		for(char ch: v){
			vowels.add(ch);
		}
		for(char ch: c){
			consonants.add(ch);
		}
		//Determines longest subseqeunce of alternating vowels / consonants
		for(int i = 0; i <= s.length() - 1; i++){
			StringBuilder sb = new StringBuilder();
			boolean vowel =  vowels.contains(s.charAt(0));
			for(int j = 0; j <= i; j++){
				char curr = s.charAt(j);
				if(vowel && vowels.contains(curr)){
					sb.append(curr);
					vowel = false;
				} else if(!vowel && consonants.contains(curr)){
					sb.append(curr);
					vowel = true;
				}
			}
			String str = sb.toString();
			int length = sb.toString().length();
			//Stores longest string and maps length to possible solutions of same length
			if(length >= max){
			    longest = str;
				max = length;
				if(map.containsKey(length)){
					List<String> list = map.get(length);
					list.add(longest);
					map.put(length, list);
				} else{
					List<String> list = new ArrayList<>();
					list.add(longest);
					map.put(length, list);
				}
			}
		}
		longest = maxString(map, max);
		return longest;
	}
	/**
	Calculates maximum string based on strings with lengths 
	equal to the longest subsequence length ASCII sum 
	**/
	public static String maxString(HashMap<Integer, List<String>> map, int length){
		int sum = 0, max = 0;
		String result = null;
		List<String> list = map.get(length);
		for(String s: list){
			sum = 0;
			for(int i = 0; i < s.length(); i++){
				sum += s.charAt(i) - 'a';
			}
			if(sum > max){
				max = sum;
				result = s;
			}
		}
		return result;

		
	}
}