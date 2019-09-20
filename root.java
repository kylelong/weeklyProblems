class root{
    public static void main(String [] args){
        int [] squares = new int[]{2, 4, 9, 16, 25, 36, 49};
        for(int s: squares){
            System.out.println(root(s, 2));
        }
    }
     static double root(double x, int n) {
      // your code goes here
      double low = 0;
      double high = x;
      double mid = 0.0;
      while(low <= high){
        mid = (high + low) / 2;
        if(Math.pow(mid, n) > x){
          
          high = mid;
        }
        if(Math.pow(mid, n) < x){
          low =  mid;
        }
        
        if(Math.abs(Math.pow(mid, n) - x) <= 0.001){
          return Math.round(mid);
        }
      }
    return Math.round(mid);
    
  }
}