import java.util.Stack;
import java.util.Scanner;
public class Evenup {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int numCards = sc.nextInt();
        Stack<Integer> s = new Stack<Integer>();
        while(sc.hasNext()) {
            int next = sc.nextInt();
            if(!s.isEmpty()){
                if((s.peek() + next) %2 ==0) {
                    s.pop();
                } else {
                    s.push(next);
                }
            } else {
                s.push(next);
            }
            
        }
        System.out.println(s.size());
    }
}
}
