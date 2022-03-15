
import java.util.ArrayList;
import java.util.Stack;

public class Solution2 {
    public String[] solution(String[] records) {


        ArrayList<String> save = new ArrayList<>();
        Stack<String> namealarm = new Stack<>();
        Stack<String> activealarm = new Stack<>();



        for(int i=0; i<records.length; i++){
            // tmpstr[0] << 이름이다 // tmpstr[1] << 동작이다.
            String[] tmpstr = records[i].split(" ");
            //이름 tmpstr[0]
            //동작 tmpstr[1]

            switch (tmpstr[1]){
                //알림창에서 보관함으로 이동시킬때
                case "notification":
                    String names = namealarm.pop();
                    String actives = activealarm.pop();
                    int count = 0;
                    boolean whileTrue = true;


                    while(whileTrue){
                        names = names;
                        count = count;
                        String beforeact = activealarm.peek();
                        if (beforeact.equals(actives)){
                            names = namealarm.pop() + " and " + names;
                            actives = activealarm.pop();
                            count ++;

                        }else{
                            whileTrue = false;
                        }
                        if(activealarm.size() == 0){
                            whileTrue = false;
                        }
                    }
                    if(count <= 1){
                        if(actives.equals("share")){
                            save.add(names + " shared your post");
                        }else{
                            save.add(names + " commented on your post");
                        }
                    }else{
                        String[] tmp = names.split(" ");

                        if(actives.equals("share")) {
                            save.add(tmp[0] + " and " + count + " others shared your post");
                        }else{
                            save.add(tmp[0] + " and " + count +  " others commented on your post");
                        }
                    }

                    break;
                //check notifi- 가 아니면 일단 스택에 넣고본다.
                default:
                    namealarm.push(tmpstr[0]);
                    activealarm.push(tmpstr[1]);
            }

        }


        String[] answer = new String[save.size()];
        answer = save.toArray(answer);
        return answer;
    }

    public static void main(String[] args){
        Solution2 solu = new Solution2();
        String[] arr = {
                "john share", "mary comment", "jay share", "check notification", "check notification", "sally comment", "james share", "check notification", "lee share", "laura share", "will share", "check notification", "alice comment", "check notification"
        };
        String[] tmp = solu.solution(arr);
        for(int i=0; i<tmp.length; i++){
            System.out.println(tmp[i]);
        }
    }
}
