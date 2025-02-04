class Solution {
    fun solution(book_time: Array<Array<String>>): Int {
        var answer: Int = 0
        
        val bookList = book_time.toList().sortedBy { it.first() };
        var bookedRooms = mutableListOf<Time>();
        
        for(book in bookList) {
            var startArr = book[0].split(":")
            var endArr = book[1].split(":");
            
            var startTm = startArr[0].toInt()*60 + startArr[1].toInt();
            var endTm = endArr[0].toInt()*60 + endArr[1].toInt() + 10;
            
            if(bookedRooms.size == 0) bookedRooms.add(Time(startTm, endTm));
            else {
                var checked = true;
                for(i in 0 until bookedRooms.size) {
                    if(bookedRooms[i].end <= startTm) {
                        checked = false;
                        bookedRooms[i] = Time(startTm, endTm);
                        break;
                    }
                }
                
                if(checked) bookedRooms.add(Time(startTm, endTm))
            }
        }
        answer = bookedRooms.size
        return answer
    }
    
    data class Time(val start:Int, val end:Int)
}