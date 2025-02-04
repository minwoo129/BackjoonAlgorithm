class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var newPlayers = players;
        val playerMap = HashMap<String, Int>();
        
        for(i in 0..players.size-1) {
            playerMap.put(players[i], i);
        }
        
        for(i in 0..callings.size-1) {
            var call = callings[i];
            var idx = playerMap.getOrDefault(call, 0);
            var change = newPlayers[idx-1];
            newPlayers[idx-1] = call;
            newPlayers[idx] = change;
            playerMap.put(call, idx-1);
            playerMap.put(change, idx)
        }
        
        return newPlayers;
    }
}