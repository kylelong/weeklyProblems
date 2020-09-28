import java.util.*;

class Asteroids {
    public static void main(String[] args) {
        int[] arr = { 5, 10, -5 };
        System.out.println(Arrays.toString(asteroidCollision(arr))); // [5, 10]

    }

    /**
     * Rules: 1. If two astroid meet the smaller will explode. 2. If both asteroids
     * are the same size, both will explode 3. Two asteroids moving in the same
     * direction will never meet (collide) Use ArrayList to add all asteroids. for
     * list.size() - 1 .. 0 get the first asteroid (i) get the second asteroid (i -
     * 1) // if in bounds
     * 
     **/
    public static int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int a : asteroids) {
            while (!stack.isEmpty() && a < 0 && stack.peek() > 0 && Math.abs(stack.peek()) < Math.abs(a)) {
                stack.pop();
            }
            if (stack.isEmpty() || a > 0 || stack.peek() < 0) {
                stack.push(a);
            } else if (Math.abs(a) == Math.abs(stack.peek())) {
                stack.pop();
            }

        }
        int[] arr = new int[stack.size()];
        Collections.reverse(stack);
        for (int i = 0; i < arr.length; i++) {
            arr[i] = stack.pop();
        }
        return arr;
    }
}