import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, K;
	
	static Queue<Integer> queue = new LinkedList<>();
	static List<Object> result = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= N; i++) {
			queue.add(i);
		}
		
		result.add("<");
		
		josephusPermutation();
		
		for (Object obj : result) {
			System.out.print(obj);
		}
	}
	
	private static void josephusPermutation() {
		while(!queue.isEmpty()) {
			for (int i = 0; i < K-1; i++) {
				queue.offer(queue.poll());
			}
			
			if(queue.size() > 1) {
				result.add(queue.poll());
				result.add(", ");
			} else {
				result.add(queue.poll());
				result.add(">");
			}
		}
	}
}
