inputs = File.read("day06_input.txt").split(",").map(&:to_i)
fishies = Array.new(9, 0) # 0 1 2 3 4 5 6 7 8
inputs.each {|i| fishies[i] += 1 }
days = 256
days.times do
  fishies[7] += fishies[0] # 0 -> 7
  p fishies = fishies.rotate(1) # 0 -> 8
end
p fishies.sum
