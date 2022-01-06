require "parallel"

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

def paralle_update(fishies, days)
  fishies = Parallel.map(fishies, in_process: 8) do |fish|
    day = 0
    fish = [fish]
    loop do
      break if day == days
      fish = update(fish)
      day += 1
    end
    fish
  end
  fishies.flatten
end

line = gets
fishies = line.chomp.split(",").map(&:to_i)
days = 256
para = 4
para.times do
  fishies = paralle_update(fishies, days/para)
  p fishies.size
end
