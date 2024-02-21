import static java.lang.Math.*;

import java.util.Scanner;

public class Main {
	public static void getLCM(int n, int m) {
		int answer = max(n, m);
		while (true) {
			if (answer % n == 0 && answer % m == 0) {
				System.out.println(answer);
				break;
			} else {
				answer += answer;
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		getLCM(n, m);
	}
}