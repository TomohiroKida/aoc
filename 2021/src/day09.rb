require "pp"

def func1(inputs)
  cnt = 0
  imax = inputs.size
  jmax = inputs[0].size
  for i in 0..imax-1 do
    for j in 0..jmax-1 do
      target = inputs[i][j]
      up     = (i-1 > -1    ) ? inputs[i-1][j] : 9
      down   = (i+1 < imax  ) ? inputs[i+1][j] : 9
      left   = (j-1 > -1    ) ? inputs[i][j-1] : 9
      right  = (j+1 < jmax  ) ? inputs[i][j+1] : 9
      #puts "#{left} #{right} #{up} #{down} : #{target}"
      cnt += target+1 if target < left  && 
                         target < right && 
                         target < up    && 
                         target < down
    end
  end
  p cnt
end

def is_bound_of_area(i, j, imax, jmax)
  if i >= 0 && i < imax && j >= 0 && j < jmax
    return false
  else
    return true 
  end
end

# basin is low point
def basinsize(areas, basin)
  i = basin.first
  j = basin.last
  t = areas[i][j]
  imax = areas.size
  jmax = areas[0].size
  arounds = [basin]
  for oi in -1..1 do
    for oj in -1..1 do
      next if oi.abs == oj.abs
      next if is_bound_of_area(i+oi, j+oj, imax, jmax)
      ai = i+oi
      aj = j+oj
      w = areas[ai][aj]
      next if w == 9
      if w > t
        new_basin = [ai, aj] 
        arounds += basinsize(areas, new_basin)
      end
    end
  end
  return arounds
end

def func2(areas)
  p imax = areas.size
  p jmax = areas[0].size
  basins = []
  for i in 0..imax-1 do
    for j in 0..jmax-1 do
      t = areas[i][j]
      u = (i-1 > -1    ) ? areas[i-1][j] : 9
      d = (i+1 < imax  ) ? areas[i+1][j] : 9
      l = (j-1 > -1    ) ? areas[i][j-1] : 9
      r = (j+1 < jmax  ) ? areas[i][j+1] : 9
      basins << [i, j] if t < u && t < d && t < l && t < r
    end
  end
  basinsizes = []
  basins.each do |basin|
    arounds = basinsize(areas, basin)
    basinsizes << arounds.uniq.size
  end
  p three_largest_basines = basinsizes.sort.reverse[0..2]
  p three_largest_basines.inject(&:*)
end

#inputs = File.open("./data/day09_input.txt")
inputs = File.open("./data/day09_input_test.txt")
p inputs = inputs.each_line.map{|l| l.chomp.split("").map(&:to_i) }
func1(inputs)
func2(inputs)
