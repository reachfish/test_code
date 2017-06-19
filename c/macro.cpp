//常用宏 
#include <iostream>
#include <cstdio>
using namespace std; 

//--------------------------------------------------------------------------------
//                  # 和 ##
//包含语句;或者多个语句的宏时，使用do...while(0)，否则会引入;错误或者宏被切分错误
//1. 单个#字符串化，表示在宏变量前后加上"
#define PRINT(EXP) \
    do { \
        cout<<#EXP<<" = "<<EXP<<endl; \
    } while(0)

//2. 双##表示拼接，并且可以使用多个##来拼接
#define TYPE(id,type,init)   type id##_##type##_##init  = init
void sharp_test(){
    int a = 10;
    PRINT(a);  //a = 10

    TYPE(b, int, 20);
    PRINT(b_int_20); //b_int_20 = 20
}
//--------------------------------------------------------------------------------
//              可变参数
//1. __VA_ARGS__ 表示可变参数              
#define debug_err(format, ...) fprintf(stderr, format, __VA_ARGS__)
//2. xxx... 表示可变参数重命名为xxx
//   ## 表示去掉前面逗号
#define debug(format, args...) printf(format, ## args)
void vargs_test(){
    debug_err("[error]code=%d,msg=%s\n", 200, "test ok");
    debug("succ\n");
}
//--------------------------------------------------------------------------------

int main(){
    sharp_test();
    vargs_test();

    return 0;
}
