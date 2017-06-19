object FirstClassFunction{
  def test() = {
          //sum of f(i) from a to b
          def sum1(f: Int => Int, a: Int, b:Int):Int =
            if (a>b) 0 else f(a) + sum1(f, a+1,b)

          //currying
          def sum2(f: Int=>Int):(Int, Int)=>Int = {
            def sumF(a: Int, b: Int):Int = {
              if (a>b) 0 else f(a) + sumF(a+1, b)
            }
            sumF
          }

          var sumX = sum2(x => x)
          var sumX2 = sum2(x => x*x)

          println("sumX(1,4)="+sumX(1,4))
          println("sumX2(1,4)="+sumX2(1,4))
  }

  def main(args: Array[String]):Unit = {
          test()
  }
}
