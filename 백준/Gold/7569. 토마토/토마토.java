import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static class tomato {
		int x;
		int y;
		int z;
		
		public tomato(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
	}
	
	private static int N, M, H;
	private static int[][][] tomatos;
	
	private static Queue<tomato> queue = new LinkedList<>();
	
	private static int[] dx = {-1, 1, 0, 0, 0, 0};
	private static int[] dy = {0, 0, -1, 1, 0, 0};	
	private static int[] dz = {0, 0, 0, 0, 1, -1};	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		
		tomatos = new int[H][N][M];
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < N; j++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int k = 0; k < M; k++) {
					tomatos[i][j][k] = Integer.parseInt(st.nextToken());
					
					if(tomatos[i][j][k] == 1) {
						queue.offer(new tomato (j, k, i));
					}
				}
			}
		}
		
		System.out.println(bfs());

	}
	
	private static int bfs() {
		while(!queue.isEmpty()) {
			tomato ripeTomato = queue.poll();
			int tx = ripeTomato.x;
			int ty = ripeTomato.y;
			int tz = ripeTomato.z;
			
			for (int i = 0; i < 6; i++) {
				int nx = tx + dx[i];
				int ny = ty + dy[i];
				int nz = tz + dz[i];
				
				if(nx < 0 || ny < 0 || nz < 0 || nx >= N || ny >= M || nz >= H) continue;
				
				if(tomatos[nz][nx][ny] == 0) {
					tomatos[nz][nx][ny] = tomatos[tz][tx][ty] + 1;
					queue.add(new tomato(nx, ny, nz));
				}
			}
		}
		
		int max = Integer.MIN_VALUE;
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < M; k++) {
					// 익지 않은 토마토가 있으면 -1
					if(tomatos[i][j][k] == 0) {
						return -1; 
					}
					
					// 토마토가 다 익는데 걸리는 시간 계산
					if(max < tomatos[i][j][k]) {
						max = tomatos[i][j][k];						
					}
				}
			}
		}
		
		if(max == 1) { // 처음부터 토마토가 다 익어있었다면
			return 0;
		} else {
			return max - 1;
		}
	}
}