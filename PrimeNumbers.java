import java.util.ArrayList;

class PrimeNumbers{
    private boolean isPrime(long number){
        for(long i = 2; i < number; ++i){
            if(number % i == 0)
                return false;
        }
        return true;
    }

    private ArrayList<Long> getPrimes(int totalPrimes){
        int count = 0;
        long iterator = 2;
        ArrayList<Long> primeLists = new ArrayList<>();
        while(count != totalPrimes){
            if(this.isPrime(iterator)){
                primeLists.add(iterator);
                ++count;
            }
            ++iterator;
        }
        return primeLists;
    }

    public static void main(String[] args) {
        
    }
}