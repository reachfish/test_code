//常用宏 
#include <iostream>
using namespace std; 

//包含语句;或者多个语句的宏时，使用do...while(0)，否则会引入;错误或者宏被切分错误
//单个#字符串化，表示在宏变量前后加上"
#define PRINT(EXP) \
    do { \
        cout<<#EXP<<" = "<<EXP<<endl; \
    } while(0)

//双##表示拼接，并且可以使用多个##来拼接
#define TYPE(id,type,init)   type id##_##type##_##init  = init

void sharp_def(){
    int a = 10;
    PRINT(a);  //a = 10

    TYPE(b, int, 20);
    PRINT(b_int_20); //b_int_20 = 20
}

int main(){
    sharp_def();

    return 0;
}
