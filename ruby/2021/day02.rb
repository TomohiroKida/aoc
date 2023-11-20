inputs = File.read("data/day02_input.txt").scan(/([fud]).* (\d*)/).map {|c, v| (c == 'u') ? [c, -v.to_i] : [c, v.to_i]}
# 2322630
p inputs.inject([0, 0]) {|r, (c, v)| if (c=='f'); r[0] += v; else r[1]+= v; end ;r }.inject(:*)
# 2105273490
p inputs.inject([0, 0, 0]) {|r, (c, v)| if (c=='f'); r[0] += v; r[1] += r[2]*v; else r[2]+= v; end ;r }.first(2).inject(:*)
