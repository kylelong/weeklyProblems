import java.util.*;
/** 
Given an array of integers arr, a pair (n,m) is called “special” if arr[n] == arr[m], and n < m. 
Return the number of special pairs. Hint: Nested for loops can work for this one, but a hashmap 
solution will have a better runtime!

Examples:
$ specialPairs([1,2,3,1,1,3])
$ 4 // (0,3), (0,4), (3,4), (2,5)
**/
public class SpecialPairs{

	public static void main(String [] args){
		System.out.println(specialPairs(new int[]{1,2,3,1,1,3})); //4d

	}
	/**
	Returns the numbers of pairs (n,m) where arr[n] == arr[m], and n < m
	@param array an array of integers
	@returns number of pairs satisfying the condition above
	 **/
	public static int specialPairs(int [] array){
		HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
	    int pairs = 0;
		for(int i = 0; i < array.length; i++){
			int num = array[i];
			if(map.containsKey(num)){
				ArrayList<Integer> list = map.get(num);
				list.add(i);
				map.put(num, list);
				for(int n: list){
					if(i != n){
						pairs++;
					}
				}
			} else{
				ArrayList<Integer> list = new ArrayList<>();
				list.add(i);
				map.put(num, list);
			}
		}
		return pairs;
	}
}