require "pp"

def calMapSize(coords)
  xsize = 0
  ysize = 0
  coords.each_cons(2) do |(x1, y1), (x2, y2)|
    xsize = [x1, x2, xsize].max
    ysize = [y1, y2, ysize].max
  end
  return xsize+1, ysize+1
end

def createMap(coords)
  xsize, ysize = calMapSize(coords)
  p xsize, ysize
  map = Array.new(ysize) { Array.new(xsize, 0) }
  coords.each_cons(2) do |(x1, y1), (x2, y2)|
    y1.step(y2, (y2-y1)/(y2-y1).abs) { |y| map[y][x1] += 1 } if x1 == x2 
    x1.step(x2, (x2-x1)/(x2-x1).abs) { |x| map[y1][x] += 1 } if y1 == y2
    if x1 != x2 && y1 != y2
      x = x1
      y = y1
      ((x2-x1).abs+1).times do
        map[y][x] += 1 
        x = x + (x2-x1)/(x2-x1).abs
        y = y + (y2-y1)/(y2-y1).abs
      end
    end
  end
  return map
end
p coords = File.read("day05_input.txt").scan(/(\d+),(\d+)/).map {|l| l.map(&:to_i) }
map = createMap(coords)
pp map
p map.flatten.select {|n| n >= 2 }.size
