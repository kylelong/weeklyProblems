import java.util.Arrays;

class Zeros {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 0, 1, 0, 0, 3, 6 };
        System.out.println(Arrays.toString(moveZeros(arr))); // [1, 2, 1, 3, 6, 0, 0, 0]
    }

    /**
     * Moves all zeros in an array to the end
     * 
     * @param arr array to manipulate
     * @return array with zeros at the end
     */
    public static int[] moveZeros(int[] arr) {
        if (arr == null || arr.length == 0)
            return null;
        int index = 0;
        for (int n : arr) {
            if (n != 0) {
                arr[index++] = n;
            }
        }
        // places zeros at end
        // index == arr.length if no zeros exists
        while (index < arr.length) {
            arr[index++] = 0;
        }
        return arr;
    }
}