import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static int N, M;
	private static int[][] tomatos;
	
	private static Queue<int[]> queue = new LinkedList<>();
	
	private static int[] dx = {-1, 1, 0, 0};
	private static int[] dy = {0, 0, -1, 1};	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		tomatos = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				tomatos[i][j] = Integer.parseInt(st.nextToken());
				
				if(tomatos[i][j] == 1) {
					queue.offer(new int[] {i, j});
				}
			}
		}
		
		System.out.println(bfs());
	}
	
	private static int bfs() {
		while(!queue.isEmpty()) {
			int [] ripeTomato = queue.poll();
			int tx = ripeTomato[0];
			int ty = ripeTomato[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = tx + dx[i];
				int ny = ty + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
				
				if(tomatos[nx][ny] == 0) {
					tomatos[nx][ny] = tomatos[tx][ty] + 1;
					queue.add(new int[] {nx, ny});
				}
			}
		}
		
		int max = Integer.MIN_VALUE;
		
		if(checkZero()) {
			return -1;
		} else {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if(max < tomatos[i][j]) max = tomatos[i][j] - 1; 
				}
			}
		}
		
		return max;
	}
	
	// 덜 익은 토마토가 있는지 확인하는 메소드
	// 하나라도 덜 익었으면 true, 다 익었으면 false
	private static boolean checkZero() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(tomatos[i][j] == 0) return true;
			}
		}
		return false;
	}
}
