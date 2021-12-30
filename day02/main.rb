class Dive
  attr_accessor :ls
  attr_accessor :pos
  attr_accessor :dep
  attr_accessor :aim
  def initialize
    @ls = []
    @pos = 0
    @dep = 0
    @aim = 0
    while 1 do
      line = gets
      break if line == nil
      @ls << line.split(" ")
    end
  end
  def command1(cmd, val)
    @pos += val if cmd == "forward"
    @dep -= val if cmd == "up"
    @dep += val if cmd == "down"
  end
  def command2(cmd, val)
    if cmd == "forward"
      @pos += val      
      @dep += @aim*val
    end
    @aim -= val      if cmd == "up"
    @aim += val      if cmd == "down"
  end
  def run
    @ls.each do |l|
      cmd = l[0] 
      val = l[1].to_i
      command2(cmd, val)
      #puts "#{cmd} #{val}"
    end
    return @pos * @dep
  end
end
d = Dive.new
p d.run
