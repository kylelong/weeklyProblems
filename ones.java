public class ones {
    public static void main(String[] args) {
        System.out.println(numberOfOnes(2)); // 1
        System.out.println(numberOfOnes(3)); // 2
        System.out.println(numberOfOnes(4)); // 1
        System.out.println(numberOfOnes(7)); // 3
        System.out.println(numberOfOnes(15)); // 4
        System.out.println(numberOfOnes(30)); // 4
        System.out.println(numberOfOnes(500)); // 6
        System.out.println(numberOfOnes(25)); // 3
        System.out.println(numberOfOnes(2020)); /// 7
    }

    public static int numberOfOnes(int n) {
        int count = 0;
        while (n != 0) {
            if (n % 2 != 0) {
                count++;
            }
            n /= 2;
        }
        return count;
    }
}