/**
 * Created by kylel95 on 11/3/18.
 */
import java.util.*;
public class fiftysum {
    public static void main(String [] args){
        int [] arr = new int[101];
        int index = 0;
        for(int i = -50; i <= 50; i++){
            arr[index] = i;
            index++;
        }
        int n = 45;
        List<String> list = allPairs(n, arr);
        if(list.size() == 0){
            System.out.println("No pairs were found.");
        }
        else {
            for (String s : list) {
                System.out.println(s);
            }
        }


    }
    public static List<String> allPairs(int n, int [] arr){
        List<String> list = new ArrayList<>();
        for(int i : arr){
            for(int j: arr){
                if(i + j == n){
                    StringBuilder sb = new StringBuilder();
                    sb.append("(");
                    sb.append(i);
                    sb.append(",");
                    sb.append(j);
                    sb.append(")");
                    list.add(sb.toString());

                }
            }
        }
        return list;
    }
}
