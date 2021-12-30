def largeMeasure(ns)
  bef = nil
  inc = 0
  ns.each do |num|
    bef = num if bef == nil
    inc += 1 if num > bef
    bef = num  
  end
  return inc
end
def largeThreeMeasure(ns)
  bef = nil
  inc = 0
  (ns.size-2).times do |i|
    sum = ns[i] + ns[i+1] + ns[i+2]
    bef = sum if bef == nil
    inc += 1 if sum > bef
    bef = sum
  end
  return inc
end
ns = []
while 1 do
  line = gets
  break if line == nil
  ns << line.to_i
end
p largeMeasure(ns)
p largeThreeMeasure(ns)
