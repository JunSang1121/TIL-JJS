import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Lotto {
    Scanner sc = new Scanner(System.in);

    public void menu(){
        System.out.println(" Lotto 프로그램");
        System.out.println("==================");
        System.out.println(" 1. Lotto 구매");
        System.out.println(" 2. 프로그램 종료");
        System.out.println("==================");
    }
    public void start(){
        while(true){
            menu();
            int a;
            System.out.print( "메뉴 선택 : ");
            a=sc.nextInt();
            if(a==1)
            {
                buy();
            }
            else if(a==2)
            {
                System.out.println();
                System.out.println("감사합니다");
                return;
            }
            else{
                System.out.println("다시 입력해주세요");
            }
        }
    }
    public void buy(){
        int money;

        System.out.println("\n Lotto 구매합니다.");
        System.out.println("[로또 구입단가 1000원]");
        System.out.print("금액 입력 : ");
        money = sc.nextInt();
        if(money<1000){
            System.out.println("1000원 이상 입력");
            return;
        }
        else if(money>10000){
            System.out.println("10000원 이하 입력");
            return;
        }

        lotto_random(money);
    }
    public void lotto_random(int money){
        Set<Integer> set = new HashSet<Integer>();
        int amount = money/1000;
        System.out.println("\n로또 번호 출력하기");
       
        for(int i=1;i<=amount;i++){
            while(set.size()<6){
                set.add((int)(Math.random()*45+1));
            }
            ArrayList<Integer> list = new ArrayList<Integer>(set);
            Collections.sort(list);
            System.out.println("로또 번호"+ i +list);
            set.clear();
        }
        
        System.out.println("받은 금액은 "+money+"원이고, 거스름돈은 "+money%1000+"원 입니  다.\n");
    }
    public static void main(String[] args) {
        new Lotto().start();
    }
}