import java.util.TreeMap;

public class RRN {

     
    public void RRN_start(){
        TreeMap<Integer,Integer> map = new TreeMap<Integer,Integer>();
        for(int i=0;i<5;i++)
        {
            map.put(i,i+1);
        }
        System.out.println("이름 \t 주민번호");
        for(int i : map.keySet())
        {
            System.out.println(i+"\t"+map.get(i));
        }
    }   
    public static void main(String[] args) {
        new RRN().RRN_start();
    }
}
