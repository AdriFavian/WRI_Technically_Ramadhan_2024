public class SpinWords {
    public static String spinWords(String sentence) {
        String [] splitWords = sentence.split(" ");
        for (int i=0; i<splitWords.length; i++) {
            if(splitWords[i].length() >= 5) {
                splitWords[i] = reverseWords(splitWords[i]);
            }
        } 
        return String.join(" ", splitWords);
    }

    public static String reverseWords(String str){
        StringBuilder result = new StringBuilder();
        for(int j = str.length() - 1; j >= 0; j--){
            result.append(str.charAt(j));
        }
        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(spinWords("Hey fellow warriors"));
        System.out.println(spinWords("This is a test"));
        System.out.println(spinWords("This is another test"));
    }
}