; this is a comment line

;定义变量
(define x 123)

;改变变量值
(set! x 200)

;true false
(set! x #t)
(set! x #f)

;数字型
;复数
(define c 3+2i)
;实数
(define f 5/6)
;有理数
(define p 3.14)
;整数  #b, #d, #o, #x 二、十、八、十六制整数
(define i #x33)

;单个字符,以#\开头的单个字符，特殊情况: #\space  #\newline 
(define c #\a)
;字符串，""括起来
(define s "hello")
(define ss (string #\h #\e #\l #\l #\o))
;取长度
(string-length s )
;更改单个字符
(string-set! s 0 #\B)
;取单个字符
(string-ref s 1)
;字符串中的"用 \"来表示

;符号型, 相当于C中的枚举，'和quote的作用是一样的
(define a (quote xyz))
(define b 'xyz)

;pair
(define p (cons 4 5))
(car p)
(cdr p)
(set-car! p 1)
(set-cdr! p 1)

;list 
(define l (list 1 2 3 4))
(define l (make-list 5 6))

;vector 
(define v #(1 2 3 4))
(define v (vector 1 2 3 4))

;判断值类型  (type? val)
(char? #\A)

;判断相等
(define l (list 1 2 3 4))
(define d (list 1 2 3 4))
;eq? 判断两个参数是否指向同一个对象
(eq?  l d) ;#f
;equal?判断两个参数是否有相同的内容
(equal? l d) ;#t

;类型转换
;t1->t2
(integer->char 97)

;函数  lambda 
(define foo (lambda(x) (* x x)))
;也可以不用lambda直接（函数名 参数)这样定义
(define (foo x) (* x x))

;匿名函数，用lambda来直接代替函数名
((lambda (x)(* x x))  5)

;过程嵌套定义 
;(define foo (lambda (x y z) 
;                    (
;                      (define add (lambda(a b) (+ a b)))
;                      (- x (add y z))
;                     )
;            )
;)

;顺序结构 
;(begin  form1  form2 ...)

;if结构
;(if (condition) (do form) (else form))

;switch机构
;(cond ((case1) form1) ((case2) form2) ... (else form))

;局部变量
;define是全局变量 
;let是局部变量
;(let ((a 10)))

;list的集合操作
;apply, 将集合中的每个元素都应用函数
;(define sum(l) (apply + l))
;map，将后面多个list中的对应位置元素都应用函数，并返回一个list
;(define sum(l1 l2)(map + l1 l2))

;逻辑 
; and 当中有一个是#f时，返回#f，否则返回最后一个元素
; or 当中有一个是#t时，返回#t，否则返回最后一个元素 
; 类似lua


(define (list-remove ls x)(
                if (null? ls) '() (
                    let ((h (car ls))   (t (list-remove (cdr ls) x)))
                    (if (= h x) t (cons h t))
                )
        )
)

(display (list-remove  (list  1  2 3 4 1 5 1) 1))

(define (list-find ls x i)(
                if (null? ls) #f (
                    let ((cur  (if (null? i) 0 i)))
                    (if (= (car ls) x) cur (list-find (cdr ls) x (+ 1 cur)))
                )
        )
)

(display (list-find  (list 1 2 3 4 5) 3  0))
