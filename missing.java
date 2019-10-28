/**
 * Given a list of ordered integers with some of the numbers missing (and with possible duplicates),
 *  find the missing numbers.
 * */
import java.util.*;
public class missing{

    public static void main(String [] args){
        ArrayList<Integer> list =  missingInt(new int[]{1, 3, 3, 5, 6});
        System.out.println(list.toString()); //2, 4
        list =  missingInt(new int[]{1, 2, 3, 4, 4, 7, 7});
        System.out.println(list.toString()); //5, 6

    }
    /**
     * Generates list of missing numbers from an array inclusive. 
     * @param nums array to check for missing numbers in
     * @return list of missing numbers
     */
    public static ArrayList<Integer> missingInt(int [] nums){
        int min = nums[0];
        int max = nums[nums.length - 1];
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = min; i < max; i++){
            if(binarySearch(nums, i) == -1){
                list.add(i);
            }
        }
        return list;
    }
    /**
     * Binary search algorithm on a sorted array to check if an element is in the array
     * @param nums array to check for target in
     * @param target element to search for
     * @return whether the element is in the array or not
     */
    public static int binarySearch(int [] nums, int target){
        int low = 0;
        int high = nums.length - 1 ;
        while(low <= high){
            int mid = low + ((high - low) / 2);
            if(nums[mid] < target){
                low = mid + 1;
            } else if(nums[mid] > target){
                high = mid - 1;
            } else{
                return mid;
            }
         

        }

        return -1;

    }

}