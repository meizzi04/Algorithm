import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static int N, M;
	static int[][] map;
	static boolean[][] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(countYear());
	}
	
	private static int countYear() {
		int year = 0;
		
		while(true) {
			int ice = countIce();
			
			if(ice == 0) { // 빙산이 다 녹았는데 분리되지 않은 경우 0 출력
				year = 0;
				break;
			} else if(ice >= 2) { // 빙산이 두 덩어리 이상으로 분리된 경우 break
				break;
			}
			
			bfs(); // 빙산 녹이기
			year++;
		}

		return year;
	}
	
	private static int countIce() {
		visited = new boolean[N][M];
		int ice = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(!visited[i][j] && map[i][j] > 0) {
					dfs(i, j);
					ice++;
				}
			}
		}
		
		return ice;
	}
	
	private static void dfs(int x, int y) {
		visited[x][y] = true;
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
			
			if(!visited[nx][ny] && map[nx][ny] > 0) {
				dfs(nx, ny);
			}
		}
	}
	
	private static void bfs() {
		Queue<int[]> queue = new LinkedList<>();
		visited = new boolean[N][M];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(map[i][j] > 0) {
					queue.add(new int[] {i, j});
					visited[i][j] = true;
				}
			}
		}
		
		while(!queue.isEmpty()) {
			int[] ice = queue.poll();
			int x = ice[0];
			int y = ice[1];
			
			int sea = 0;
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

				if(!visited[nx][ny] && map[nx][ny] == 0) {
					sea++;
				}
			}
			
			if(map[x][y] - sea <= 0) {
				map[x][y] = 0;
			} else {
				map[x][y] -= sea;
			}
		}
	}
	
}
