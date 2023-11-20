def func1(inputs)
  cnt = 0
  inputs.map {|line| 
    line.split(" | ")[1].split(" ") {|str|
      case str.size
      when 2, 3, 4, 7
        cnt += 1
      end
    }
  }
  cnt
end

def value2number(value)
  case(value)
  #     0     1       2      3      4      5      6
  when [true , true , true , true , true , true , false] then "0"
  when [false, true , true , false, false, false, false] then "1"
  when [true , true , false, true , true , false, true ] then "2"
  when [true , true , true , true , false, false, true ] then "3"
  when [false, true , true , false, false, true , true ] then "4"
  when [true , false, true , true , false, true , true ] then "5"
  when [true , false, true , true , true , true , true ] then "6"
  when [true , true , true , false, false, false, false] then "7"
  when [true , true , true , true , true , true , true ] then "8"
  when [true , true , true , true , false, true , true ] then "9"
  end
end

def analysis(patterns, values)
  p patterns
  p _1 = patterns.select{|pattern| pattern.size == 2}.join
  p _4 = patterns.select{|pattern| pattern.size == 4}.join
  p _7 = patterns.select{|pattern| pattern.size == 3}.join
  p _8 = patterns.select{|pattern| pattern.size == 7}.join
  p _2_3_5 = patterns.select{|pattern| pattern.size == 5}
  p _3_5 = _2_3_5.filter{|v| v.include? _1[0]}
  p _3 = _3_5.filter{|v| v.include? _1[1]}.join
  p _6_9 = patterns.select{|pattern| pattern.size == 6}

  p "digit"
  #  0
  # 5 1
  #  6
  # 4 2
  #  3
  digits = Array.new(7, "")
  p digits[0] = _7.delete(_1)

  p d_5_6 = _4.delete(_1)
  p digits[5] = d_5_6.delete(_3)
  p digits[6] = d_5_6.delete(digits[5])
  
  p d_3_4 = _8.delete(_1).delete(d_5_6).delete(digits[0])
  p digits[4] = d_3_4.delete(_3)
  p digits[3] = d_3_4.delete(digits[4])

  p _2 = _2_3_5.filter{|d| d.include? digits[4]}.join
  p _5 = _2_3_5.filter{|d| d.include? digits[5]}.join

  p d_1_2 = _1
  p digits[1] = d_1_2.delete(_5)
  p digits[2] = d_1_2.delete(digits[1])
 
  p digits
  p values
  p out = values.map {|value| value2number(digits.map {|d| value.include? d}) }.join.to_i
  return out
end

def func2(inputs)
  p data = inputs.map {|l| 
    l.split(" | ").map {|d| 
      d.split(" ").map(&:chars).map(&:sort).map(&:join) 
    } 
  }
  data.sum {|line| analysis(line[0], line[1]) }
end

p inputs = File.read("data/day08_input.txt").lines.map(&:chomp)
p func1(inputs)
p func2(inputs)
#p func2(["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"])
