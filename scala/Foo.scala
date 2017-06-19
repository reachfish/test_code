
object Foo{
        def test(): Unit = {
            //condition expression
            val x = -10
            val y = if(x > 0) x else -x

            //tail recursion
            def gcd(a:Int, b:Int):Int = if (b==0)  a else gcd(b, a%b)
            println("gcd(14,21)="+gcd(14,21))

        }

	def main(args: Array[String]): Unit = {
            test()
        }
}
