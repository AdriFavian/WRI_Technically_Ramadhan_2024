public class BitCountingTest {
    public static int countBits(int n){
        System.out.println("bilangan anda: "+ n);
        String biner = Integer.toBinaryString(n);
        System.out.println("konversi: "+ biner);
        int count = 0;
        for (int i=0; i<biner.length();i++){
            if (biner.charAt(i) =='1'){
                count++;
            }
        }
        System.out.print("Hasil: ");
        return count;
    }

    public static void main(String[] args) {
        System.out.println(BitCountingTest.countBits(1234));
        System.out.println(BitCountingTest.countBits(4));
        System.out.println(BitCountingTest.countBits(7));
        System.out.println(BitCountingTest.countBits(9));
        System.out.println(BitCountingTest.countBits(10));
    }
}

