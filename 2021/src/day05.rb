require "pp"

def dispGridMap(map)
  map.each do |l|
    l.each { |g| print g }
    puts
  end
end

def calMapLength(coords)
  xlength = 0
  ylength = 0
  coords.each_slice(2) do |(x1, y1), (x2, y2)|
    xlength = [x1, x2, xlength].max
    ylength = [y1, y2, ylength].max
  end
  return xlength+1, ylength+1
end

def moveMap(map, (x1, y1), (x2, y2))
  #puts "#{x1}, #{y1}, #{x2}, #{y2}"
  if x1 == x2 # tate line
    x = x1
    itr = y2-y1 > 0 ? 1 : -1
    y1.step(y2, itr) { |y| 
      #puts "#{x}, #{y}"
      map[y][x] += 1
    }
  end
  if y1 == y2 # yoko line
    y = y1
    itr = x2-x1 > 0 ? 1 : -1
    x1.step(x2, itr) { |x| 
      #puts "#{x}, #{y}"
      map[y][x] += 1
    }
  end
  if (x1-x2).abs == (y1-y2).abs # diagonal
  #return map
    x = x1
    y = y1
    xitr = x2-x1 > 0 ? 1 : -1
    yitr = y2-y1 > 0 ? 1 : -1
    (((x1-x2).abs)+1).times do
      #puts "#{x}, #{y}" 
      map[y][x] += 1
      x += xitr
      y += yitr
    end
  end
  return map
end

def createMap(coords)
  xlength, ylength = calMapLength(coords)
  p xlength, ylength
  map = Array.new(ylength) { Array.new(xlength, 0) }
  coords.each_slice(2) do |(x1, y1), (x2, y2)|
    map = moveMap(map, [x1, y1], [x2, y2])
  end
  return map
end

### Count coord point of number at least 2 that from-to line by input file
### Map is square points. top left is 0, 0, bottom right is defined by input file
#coords = File.read("data/day05_input_test.txt").scan(/(\d+),(\d+)/).map {|l| l.map(&:to_i) }
coords = File.read("data/day05_input.txt").scan(/(\d+),(\d+)/).map {|l| l.map(&:to_i) }
map = createMap(coords)
#dispGridMap(map)
p map.flatten.select {|n| n >= 2 }.length
