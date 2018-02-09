import java.util.*;
public class Soylent {
	public static void main(String[] args) { 
		Scanner sc = new Scanner(System.in);
		double numCases = sc.nextDouble();
		double counter = 0;
		double  numCalPerBot = 400;
		while (numCases > counter){
			double calories = sc.nextDouble();
			System.out.println((int)Math.ceil(calories/numCalPerBot));
			counter = counter + 1;
		}
	}	
}
