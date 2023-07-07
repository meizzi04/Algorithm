def solution(players, callings):
    player_ = {rank:player for rank, player in enumerate(players)}
    rank_ = {player:rank for rank, player in enumerate(players)}
    
    for i in callings:
        cur_rank = rank_[i]
        fro_rank = cur_rank - 1
        fro_player = player_[fro_rank]
        
        # player_ 딕셔너리 정렬
        player_[cur_rank] = fro_player
        player_[fro_rank] = i
        
        # rank_ 딕셔너리 정렬
        rank_[i] = fro_rank
        rank_[fro_player] = cur_rank

    return list(player_.values())