import java.util.*;

class Checker implements Comparator<Player>{

    public int compare(Player a, Player b) {
        // If 2 Players have the same score
        if(a.score == b.score){
            // Order alphabetically by name
            return a.name.compareTo(b.name);
        }

        // Otherwise, order higher score first
        return ((Integer) b.score).compareTo(a.score);
    }
}

// Java 8
class Checker implements Comparator<Player>{
    public int compare(Player a, Player b){
        if(a.score == b.score)
            return (a.name.compareTo(b.name));
        return (b.score - a.score);

    }
}