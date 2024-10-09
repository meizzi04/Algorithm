import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, L, R;
	static int[][] populations; // 각 나라의 인구수
	static boolean[][] visited;
	
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static ArrayList<int[]> list = new ArrayList<>();
	static boolean isMove = false;
	static int cnt;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		populations = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < N; j++) {
				populations[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(move());
	}
	
	private static int move() {
		while(true) {
			isMove = false;
			visited = new boolean[N][N];
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(!visited[i][j]) bfs(i, j);
				}
			}
			
			if(!isMove) {
				break;
			} else {
				cnt++;
			}
		}
		
		return cnt;
	}
	
	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();

		queue.add(new int[] {x, y});
		list.add(new int[] {x, y});

		visited[x][y] = true;
		
		while(!queue.isEmpty()) {
			int[] q = queue.poll();
			
			x = q[0];
			y = q[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
								
				if(!visited[nx][ny] 
						&& L <= Math.abs(populations[x][y] - populations[nx][ny])
						&& R >= Math.abs(populations[x][y] - populations[nx][ny])) {
					queue.add(new int[] {nx, ny});
					list.add(new int[] {nx, ny});
					visited[nx][ny] = true;
					isMove = true;
				}
			}
		}
		
		int sum = 0;
		
		for (int i = 0; i < list.size(); i++) {
			int[] tmp = list.get(i);
			sum += populations[tmp[0]][tmp[1]];
		}
		
		for (int i = 0; i < list.size(); i++) {
			int[] tmp = list.get(i);
			populations[tmp[0]][tmp[1]] = sum / list.size();
		}
		
		list.removeAll(list);
	}
}
