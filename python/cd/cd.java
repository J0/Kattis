import java.util.*;
import java.io.*;

class CD {
    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        long jack_discs = 1; // Display the string.
        long jill_discs = 1;
        while(true){
          long overallCounter = 0;
          String[] phlist = r.readLine().split(" ");
          jack_discs = Integer.parseInt(phlist[0]); // Display the string.
          jill_discs = Integer.parseInt(phlist[1]);
          if(jack_discs ==0 && jill_discs == 0){
            break;
          }
          int jillList[] = new int[1000004];
          int jackList[] = new int[1000004];
          int jackCounter = 0;
          int jillCounter = 0;
          for(int counter = 0; counter < jack_discs; counter++) {
              String[] alist = r.readLine().split(" ");
              int num = Integer.parseInt(alist[0]);
              jackList[counter] = num;

          }
          for(int other_counter = 0; other_counter < jill_discs; other_counter++) {
            String[] blist = r.readLine().split(" ");
            int other_num = Integer.parseInt(blist[0]);
            jillList[other_counter] = other_num;
          }
          while(!((jillCounter == jill_discs) || (jackCounter== jack_discs))) {
              if(jillList[jillCounter] == jackList[jackCounter]) {
                jackCounter++;
                overallCounter++;
              } else if(jillList[jillCounter] > jackList[jackCounter]){
                jackCounter++;
              } else {
                jillCounter++;
              }
          }
          System.out.println(overallCounter);
        }
    }
}
