import java.util.Map;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        Map <String, Integer> player_ = new HashMap<>();
        Map <Integer, String> rank_ = new HashMap<>();
        for(int i = 0; i < players.length; i++) {
            player_.put(players[i], i);
            rank_.put(i, players[i]);
        }
        
        for(String i : callings) {
            int cur_rank = player_.get(i);
            int fro_rank = cur_rank - 1;
            String fro_player = rank_.get(fro_rank);
            
            player_.put(fro_player, cur_rank);
            player_.put(i, fro_rank);
            
            rank_.put(fro_rank, i);
            rank_.put(cur_rank, fro_player);
        }
        String[] answer = new String[players.length];
        int cnt = 0;
        for (String i : rank_.values()){
            answer[cnt++] = i;
        }
        
        return answer;
    }
}