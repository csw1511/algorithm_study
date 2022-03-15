public class loop {
    public static void main(String[] args){
        int power = 13;
        String members[] = {"홍길동", "김길동", "김사랑", "아무개,"};

        for(int i =0; i<10; i++){
            System.out.println(i);
        }

        for(int i=0; i<4;i++){
            System.out.println(members[i]);
        }

        for(String name : members){
            System.out.println(name);

        }

        while(power > 10){
            System.out.println("go");
            power--;
        }

        System.out.println("Stop");
    }

}
