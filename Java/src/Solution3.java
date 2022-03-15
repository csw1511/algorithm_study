import java.util.ArrayList;

public class Solution3 {
    int bestcount= 0;
    int beststation = 0;


    public int[] solution(int n, int[] passenger, int[][] train) {
        int[] answer = {};

        int[] visited = new int[n+1];
        int count = 0;
        ArrayList<Integer> answerlist = new ArrayList<>();

        dfs(train, 1, visited, count, passenger, bestcount,beststation, answerlist);

        System.out.println(answerlist);




        return answer;
    }
    public void dfs(int[][] train, int v, int[] visited, int count,int[] passanger, int bestcount, int beststation, ArrayList answerlist){
        visited[v] = 1;
        count = count + passanger[v-1];

        if (count >= bestcount){
            bestcount = count;
            if (v > beststation){
                beststation = v;
            }
        }
        System.out.println(beststation + " " + bestcount);
        answerlist.add(bestcount);
        answerlist.add(beststation);

        for(int i=0; i< train.length; i++){
            if(train[i][0] == v){
                if(visited[train[i][1]]==0){
                    dfs(train, train[i][1] ,visited, count,passanger, bestcount, beststation, answerlist);
                }
            }
        }
        count --;
    }

    public static void main(String[] args) {
        Solution3 solu = new Solution3();
        int n = 6;
        int[] pass = {1,1,1,1,1,1};
        int[][] train = {
                {1,2},
                {1,3},
                {1,4},
                {3,5},
                {3,6}
        };
        solu.solution(n, pass, train);
    }
}