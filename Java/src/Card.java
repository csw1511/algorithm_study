class Card{
    int data;
    Card(int data){
        this.data = data;
    }
    void play(Card otherCard){
        if(this.data < otherCard.data){
            System.out.println("Game's up. You lose");
        }else if(this.data > otherCard.data){
            System.out.println("Game's up. You win");
        }else if(this.data == otherCard.data){
            System.out.println("Game's up. You two halve the match");
        }
    }
}