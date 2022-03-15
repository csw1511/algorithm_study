
import java.util.*;

public class Array {
    public static void main(String[] args){
        String[] cars = {"hyundai", "bmw", "benz", "toyota"};


        //배열을 String으로 바꿔줌!
        System.out.println(Arrays.toString(cars));



        String[] cars_copied = cars.clone();
        System.out.println(Arrays.toString(cars_copied));

        //배열의 선언과 조작
        System.out.println("# 1. Declare and initialize an array");
        int[] scores = {95, 100, 87, 91};
        scores[2] = 90;

        System.out.println(scores);
        for (int i=0; i<scores.length; i++){
            System.out.println(scores[i]);
        }

        //asList의 사용법. 반환값이 Arraylist이라고 했는데 List<String>이기도 한듯
        System.out.println("\n# 2. Arrays method: toString(), asList()");
        String[] carss = {"hyundai", "bmw", "benz", "toyota"};
        List<String> car_list = Arrays.asList(carss);
        System.out.println(car_list);
        System.out.println(car_list.get(1));

        //정렬임. 순서대로 오름차순, 내림차순, 구간정렬
        System.out.println("\n# 3. Arrays method: sort(array, Comparator), sort(array, int fromindex, int toindex)");
        Arrays.sort(carss);
        System.out.println(Arrays.asList(carss));

        Arrays.sort(cars, Collections.reverseOrder());
        System.out.println(Arrays.asList(carss));

        Arrays.sort(cars,0,2);
        System.out.println(Arrays.asList(carss));

        //깊은복사임
        System.out.println("\n# 4. Arrays method: copyOf, copyOfRange");
        String[] cars_copied1 = Arrays.copyOf(carss, carss.length);
        System.out.println(Arrays.asList(cars_copied1));

        String[] cars_copied2 = Arrays.copyOfRange(cars,0,2);
        System.out.println(Arrays.asList(cars_copied2));

        //2중 또는 3중 배열
        System.out.println("\n# 5. Multiple Array");
        int[][][] allScores = {
                { { 90, 85, 70, 55, 60 }, { 96, 88, 81, 91, 75 }, { 96, 88, 81, 91, 75 }, { 96, 88, 81, 91, 75 } },
                { { 91, 82, 73, 54, 65 }, { 96, 87, 88, 99, 80 }, { 91, 82, 83, 94, 75 }, { 96, 87, 88, 99, 70 } },
                { { 92, 83, 74, 55, 66 }, { 97, 88, 89, 90, 71 }, { 92, 83, 84, 95, 76 }, { 97, 88, 89, 90, 71 } } };
        System.out.println(allScores[1][2][0]);

    }
}
