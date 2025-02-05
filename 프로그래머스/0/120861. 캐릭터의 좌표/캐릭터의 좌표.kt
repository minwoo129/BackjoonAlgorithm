class Solution {
    fun solution(keyinput: Array<String>, board: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        val rightLimit = (board[0]/2);
        val leftLimit = rightLimit * -1;
        val upLimit = (board[1]/2);
        val downLimit = upLimit * -1;
        var posX = 0;
        var posY = 0;
        
        for(way in keyinput) {
            if((way == "left") && (posX > leftLimit)) {
                posX--;
            }
            else if((way == "right") && (posX < rightLimit)) {
                posX++;
            }
            else if((way == "up") && (posY < upLimit)) {
                posY++;
            }
            else if((way == "down") && (posY > downLimit)) {
                posY--
            }
        }
        
        answer = intArrayOf(posX, posY)
        return answer
    }
}