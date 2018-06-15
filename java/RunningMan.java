import java.util.*;
public class RunningMan {
	public void run() {
		Scanner sc = new Scanner(System.in);
		int dailyFlights = sc.nextInt();
		ArrayList<HashMap<String, Integer>> adjList = new ArrayList<HashMap<String, Integer>>();
		//init adjacency list
		int numCities = 1000;
		for(int j = 0; j < numCities; j++) {
			adjList.add(new HashMap<String, Integer>());
		}

		for(int counter = 0; counter < dailyFlights; counter++) {
			String source = sc.next();
			String dest = sc.next();
			System.out.println(source);
			System.out.println(dest);

		}
	}
	public static void main(String[] args) {
		RunningMan runningMan = new RunningMan();
		runningMan.run();
	}

}
