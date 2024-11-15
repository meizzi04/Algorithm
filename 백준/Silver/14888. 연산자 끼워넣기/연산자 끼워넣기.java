import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] number;
	static int[] operator = new int[4];
	
	static int maxValue = Integer.MIN_VALUE;
	static int minValue = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		number = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			number[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 4; i++) {
			operator[i] = Integer.parseInt(st.nextToken());
		}
		
		br.close();
		
		backTracking(number[0], 1);
		
		System.out.println(maxValue);
		System.out.println(minValue);
	}
	
	private static void backTracking(int num, int idx) {
		if(idx == N) {
			maxValue = Math.max(num, maxValue);
			minValue = Math.min(num, minValue);
			return;
		}
		
		for (int i = 0; i < 4; i++) {
			if(operator[i] > 0) {
				operator[i]--;
				
				switch (i) {
				
					case 0: // +
						backTracking(num + number[idx], idx+1);
						break;
					case 1: // -
						backTracking(num - number[idx], idx+1);
						break;
					case 2: // *
						backTracking(num * number[idx], idx+1);
						break;
					case 3: // /
						backTracking(num / number[idx], idx+1);
						break;
					
				}
				
				operator[i]++;
			}
		}
	}
}