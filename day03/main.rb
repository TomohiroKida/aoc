class BinaryDianotic
  attr_accessor :ls
  def initialize
    @ls = []
    while 1 do
      line = gets
      break if line == nil
      @ls << line.chomp
    end
  end
  def p1
    bit = 12
    vs = Array.new(bit, "")
    @ls.each do |l|
      l.chars.each_with_index do |s, i|
        vs[i] += s
      end
    end
    gamma   = ""
    epsilon = ""
    len = vs[0].size
    vs.each do |l|
      high = l.count("1") > len/2 
      gamma   +=  high ? "1" : "0"
      epsilon += !high ? "1" : "0"
    end
    #p gamma, epsilon
    #p gamma.to_i(2), epsilon.to_i(2)
    p gamma.to_i(2)*epsilon.to_i(2)
  end
  def p2
    # life support rating = oxygen generator rating * CO2 scrubber rating
    i  = 0
    ls = @ls
    while 1
      l1 = ls.select { |l| l[i] == "1" }
      l0 = ls.reject { |l| l[i] == "1" }
      ls = l1.size >= l0.size ? l1 : l0
      i += 1
      break if ls.size == 1
    end
    oxygen = ls[0]
    i  = 0
    ls = @ls
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
end
bd = BinaryDianotic.new
bd.p2
