#include<stdio.h>
#include<time.h>


int is_prime(long number){
    for (long i = 2; i < number; ++i){
        if(number % i == 0)
            return 0;
    }
    return 1;
}

void set_primes(long* list, int total){
    int prime_count = 0;
    long iterator = 2;
    while(prime_count != total){
        if(is_prime(iterator) == 1){
            list[prime_count++] = iterator;
        }
        iterator++;
    }
}

int main(int argc, char const *argv[])
{
    int total_primes = 0;
    printf("Enter the total number of primes numbers to display: \n");
    scanf("%d", &total_primes);

    time_t start = clock();

    long prime_lists[total_primes];
    set_primes(prime_lists, total_primes);

    for(int i = 0; i < 10; ++i){
        printf("%ld\t", prime_lists[i]);
    }
    for(int i = total_primes - 11; i < total_primes; ++i){
        printf("%ld\t", prime_lists[i]);
    }
    printf("last: %ld\n", prime_lists[total_primes - 1]);
    time_t end = clock();
    double total_time = (double) (end - start) / CLOCKS_PER_SEC;
    printf("\nTotal time: %lf\n", total_time);
    return 0;
}
