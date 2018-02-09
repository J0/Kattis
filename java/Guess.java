import java.util.*;
public class Guess {

    public static void main(String[] args){
        int upper = 1000;
        int lower = 1;
        int guess = 500;
        int limit = 11;
        int counter = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println(guess);
        while(true && counter < limit) {
            counter = counter + 1;
            String response = sc.nextLine();
            if(response.equals("lower")) {
                upper = guess - 1;
                guess = (lower + guess) / 2 ;
                System.out.println(guess);
            } else if (response.equals("higher")){
                lower = guess + 1;
                guess = (upper + guess)/2;
                System.out.println(guess);
                
            } else if(response.equals("correct")){
                System.exit(0);
            } else {
                throw new IllegalArgumentException("input error");
            }
        }
        System.exit(0);
        
    }
}
