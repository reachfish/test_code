object QuickSort{
	def quickSort(xs: Array[Int]): Array[Int] = {
            if(xs.length <= 1) xs
            else{
                    val pivot = xs(xs.length / 2)
                    Array.concat(
                            quickSort(xs filter (pivot>)),
                            xs filter (pivot==),
                            quickSort(xs filter (pivot<))
                    )
            }
	}

	def test() = {
            val xs = quickSort(Array(3,5,1,2,0))
            for(v <- xs) print(v + ",")
	}

	def main(args: Array[String]): Unit = {
            test()
	}
}
