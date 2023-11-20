inputs = File.read("data/day01_input.txt").lines.map(&:to_i)
p inputs.each_cons(2).count {|a, b| b > a }
p inputs.each_cons(4).count {|a, b, c, d| a+b+c < b+c+d }
