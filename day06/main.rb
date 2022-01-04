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

require "parallel"

line = gets
fish = line.chomp.split(",").map(&:to_i)
days = 0
loop do
  printf "%2d ", days
  #pfish(fish)
  break if days == 256
  fish = update(fish)
  days += 1
end
p fish.size
