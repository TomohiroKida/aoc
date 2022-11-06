ls = File.read("data/day03_input.txt").split("\n")
def p1 ls
  vs = Array.new(12, "")
  ls.each do |l|
    l.chars.each_with_index do |s, i|
      vs[i] += s
    end
  end
  gamma   = ""
  epsilon = ""
  vs.each do |l|
    high = l.count("1") > ls.size/2 
    gamma   +=  high ? "1" : "0"
    epsilon += !high ? "1" : "0"
  end
  #p gamma, epsilon
  #p gamma.to_i(2), epsilon.to_i(2)
  p gamma.to_i(2)*epsilon.to_i(2)
end
def p2(lss)
  # life support rating = oxygen generator rating * CO2 scrubber rating
  i  = 0
  ls = lss
  while 1
    l1 = ls.select { |l| l[i] == "1" }
    l0 = ls.reject { |l| l[i] == "1" }
    ls = l1.size >= l0.size ? l1 : l0
    i += 1
    break if ls.size == 1
  end
  oxygen = ls[0]
  i  = 0
  ls = lss
  while 1
    l1 = ls.select { |l| l[i] == "1" }
    l0 = ls.reject { |l| l[i] == "1" }
    ls = l1.size >= l0.size ? l0 : l1
    i += 1
    break if ls.size == 1
  end
  co2 = ls[0]

  p oxygen
  p co2
  p oxygen.to_i(2) * co2.to_i(2)
end
p1 ls
p2 ls
