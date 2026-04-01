import java.util.Arrays;
public class Hello {

    public static void main(String[] args) {
        // for 1d array
        int[] id={96,99,92};
        System.out.println(id);
        int[][] marks={{97,98,99},{13,45,90}};
        // for 2d array
        System.out.println(marks[0]);
        // for length
        System.out.println(marks.length);
        // for string
        String name="Aman and tanuj";
        // for substring
        System.out.println(name.substring(0,4));
        // for replace
        System.out.println(name.replace('a' , 't'));
        // for sort
        Arrays.sort(id);
        System.out.println(id[1]);

    }}