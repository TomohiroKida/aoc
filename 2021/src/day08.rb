p inputs = File.read("day08_input.txt").lines.map(&:chomp)
data = inputs.map {|l| l.split(" | ").map {|d| d.split(" ").map(&:chars).map(&:sort).map(&:join) } }
p data
