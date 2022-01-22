inputs = File.read("day07_input.txt").split(",").map(&:to_i)
p inputs.max.times.map { |pos| inputs.sum { |crub| (crub-pos).abs } }.min
p inputs.max.times.map { |pos| inputs.sum { |crub| ((crub-pos).abs)*((crub-pos).abs+1)/2 } }.min
