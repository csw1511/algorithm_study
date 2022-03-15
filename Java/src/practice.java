import java.util.ArrayList;
//import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class practice {

    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answerlist = new ArrayList<>();
        ArrayList<Double> calcrelease = new ArrayList<>();
        for(int i=0; i<progresses.length; i++){
            double bbb = (100-progresses[i])*1.0 / speeds[i];
            double aaa = Math.ceil(bbb);
            calcrelease.add(aaa);

        }
        while(calcrelease.toArray().length > 0){
            int count = 1;
            double tmp = calcrelease.remove(0);
            boolean isit = true;
            while (isit && calcrelease.toArray().length > 0){
                double abc = (double) calcrelease.toArray()[0];
                if (tmp >= abc){
                    count++;
                    calcrelease.remove(0);
                }
                else if (tmp < abc){
                    isit = false;
                }
            }
            answerlist.add(count);

        }

        int size = answerlist.size();
        return answerlist.stream().mapToInt(i->i).toArray();
    }
    public static void main(String[] args) {
        practice prac = new practice();
        int[] progress = {93, 30, 55};
        int[] speeds = {1,30,5};

        prac.solution(progress,speeds);

    }
}
