import java.util.Arrays;

class Solution1 {
    public int solution(int[] arr) {
        int answer = 0;
        Arrays.sort(arr);

        int undernum;
        int overnum;

        // 현재 answer의 최소 임계값 차이
        int beforemin = 1001;

        //j는 임계값을 의미
        for(int j = 0; j<= 255; j ++) {
            undernum = 0;
            overnum = 0;
            //i는 arr의 인덱스. arr를 완전탐색함
            for (int i = 0; i < arr.length; i++) {
                if (j <= arr[i]) {
                    overnum++;
                } else {
                    undernum++;
                }
            }
            int tmpans = Math.abs(overnum - undernum);
            if(beforemin > tmpans){
                beforemin = tmpans;
                answer = j;
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Solution1 solu = new Solution1();
        int[] arr = {1,52,125,10,25,201,244,192,128,23,203,98,154,255};
        int tmp = solu.solution(arr);
        System.out.println(tmp);
    }
}