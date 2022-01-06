require "pp"
def inputCoord
  cs = []
  while 1 do
    c = []
    line = gets
    break if line == nil
    tmp = line.chomp.split(" ")
    c << tmp.first.split(",").map(&:to_i)
    c << tmp.last.split(",").map(&:to_i)
    cs << c
  end
  return cs
end
def calMapSize(coords)
  xsize = 0
  ysize = 0
  coords.each do |coord|
    x1, y1 = coord.first # [0, 9]
    x2, y2 = coord.last  # [5, 9]
    xsize = [x1, x2, xsize].max
    ysize = [y1, y2, ysize].max
  end
  return xsize+1, ysize+1
end

def createMap(coords)
  xsize, ysize = calMapSize(coords)
  p xsize, ysize
  map = Array.new(ysize) { Array.new(xsize, 0) }
  coords.each do |coord|
    x1, y1 = coord.first # [0, 9]
    x2, y2 = coord.last  # [5, 9]
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
coords = inputCoord
#p coords
map = createMap(coords)
pp map
p map.flatten.select {|n| n >= 2 }.size
