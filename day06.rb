def pfish(fish)
  fish.each_with_index do |f, i|
    print "#{f}"
    print i < fish.size-1 ? "," : "\n"
  end
end

def update(fish)
  adds = fish.count(0)
  after = fish.map {|f| f==0 ? 6 : f-1 }
  adds.times.each { after << 8 }
  return after
end

line = gets
fishies = Array.new(9, 0) # 0 1 2 3 4 5 6 7 8
inputs = line.chomp.split(",").map(&:to_i)
inputs.each {|i| fishies[i] += 1 }
days = 256
days.times do
  # 0 -> 7
  fishies[7] += fishies[0]
  # 0 -> 8
  fishies = fishies.rotate(1)
  #p fishies
end
p fishies.sum
