import java.util.*;
public class Guess {

    public static void main(String[] args){
        int upper = 1000;
        int lower = 1;
        int guess = 500;
        Scanner sc = new Scanner(System.in);
        while(true) {
			System.out.println(guess);
			System.out.flush();
            String response = sc.nextLine().trim();

            if(response.equals("lower")) {
                upper = guess - 1;
                guess = (lower + guess) / 2;
            } else if (response.equals("higher")){
                lower = guess + 1;
                guess = (upper + guess)/2;
            } else if(response.equals("correct")){
                break;
			}
        }
        
    }
}
