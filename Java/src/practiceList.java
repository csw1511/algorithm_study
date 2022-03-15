import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Deque;

public class practiceList {
    public static void main(String args[]) {
        ArrayList pitches = new ArrayList();
        pitches.add("138");
        pitches.add("129");
        pitches.add("142");
        pitches.add(0, "133");
        pitches.add(1, "134");

        //1번 인덱스 가져오기 .get()
        System.out.println(pitches.get(1));
        //pitches의 사이즈 가져오기 .size()
        System.out.println(pitches.size());
        // 142가 들어있는지 알려주기 true/false .contains()
        System.out.println(pitches.contains("142"));
        // 129 지우기. 성공하면 알려주기 true/false .remove()
        System.out.println(pitches.remove("129"));
        // 0번 인덱스 지우고 삭제된 항목을 리턴함. pop비슷함.
        System.out.println(pitches.remove(0));

        for (int i = 0; i < pitches.size(); i++) {
            System.out.print(pitches.get(i)+" ");
        }

        //제네릭스 쓰자. 안쓰면 ArrayList안에 추가되는 객체는 Object가 되어서
        //이를 가져올땐 항상 앞에 (String)붙여서 형변환해줘야댐.
        //제네릭스 <String> 붙이면 이 형식으로 지정해서 쓰겠다는 의미니
        //이런 과정이 필요없을것이다.
        System.out.println();
        ArrayList<String> pitche1 = new ArrayList<>();
        pitche1.add("138");
        pitche1.add("129");

        String one = pitche1.get(0);  // 형 변환이 필요없다.
        String two = pitche1.get(1);  // 형 변환이 필요없다.
        System.out.println(one);
        System.out.println(two);

        //이미 만들어져있는 배열데이터를 ArrayList로 한번에 생성하기
        // import java.util.Arrays 필요함
        String[] data = {"138", "129", "142"};  // 이미 투구수 데이터 배열이 있다.
        // asList로 배열데이터를 ArrayList로 만들고, 이를 집어넣음!
        ArrayList<String> pitches2 = new ArrayList<>(Arrays.asList(data));
        System.out.println("------\n"+pitches2);  // [138, 129, 142] 출력

        // 아니면 String 자료형 자체를 여러개 직접 넣어서 전달해도 된다
        ArrayList<String> pitches3 = new ArrayList<>(Arrays.asList("138", "129", "142"));
        System.out.println("------\n"+pitches3);

        //String join - ArrayList 붙이기
        //String.join(구분자, 리스트객체) 형식인데, 리스트 각 요소에 구분자를 집어넣어줌
        //String[] pitches 같은 문자열 배열에도 사용가능하다
        ArrayList<String> pitches4 = new ArrayList<>(Arrays.asList("138", "129", "142"));
        String result = String.join(",", pitches4);
        System.out.println(result);  // 138,129,142 출력

        //ArrayList 정렬하기. import java.util.Comparator; 필요함
        //Comparator.reverseOrder()은 내림차순 정렬이다.
        ArrayList<String> pitche5 = new ArrayList<>(Arrays.asList("138", "129", "142"));
        pitche5.sort(Comparator.naturalOrder());  // 오름차순으로 정렬
        System.out.println(pitche5); // [129, 138, 142] 출력

        //자바에서의 Deque. import java.util.Deque; 필요함
        //이들을 스택과 큐로 활용하는 모습.
        System.out.println("Stack!!");
        Deque<String> stack = new ArrayDeque<>();
        stack.addFirst("Element1");
        stack.addFirst("Element2");
        stack.addFirst("Element3");
        System.out.println(stack.removeFirst());
        System.out.println(stack.removeFirst());
        System.out.println(stack.removeFirst());

        System.out.println("Queue!!");
        Deque<String> queue = new ArrayDeque<>();
        queue.addFirst("Element1");
        queue.addFirst("Element2");
        queue.addFirst("Element3");
        System.out.println(queue.removeLast());
        System.out.println(queue.removeLast());
        System.out.println(queue.removeLast());


    }
}

