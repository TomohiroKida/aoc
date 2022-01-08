require "pp"

Point = Struct.new(:value, :mark)
balls, *boards = File.read("day04_input_test.txt").split("\n\n")
balls = balls.split(",").map(&:to_i)
boards = boards.map {|b| b.lines.map {|r| r.scan(/\d+/).map{|v| Point.new(v.to_i, false) } } }
bd1 = Marshal.load(Marshal.dump(boards))

def check(board)
  5.times.each do |r|
    bingo_row = true
    bingo_col = true
    5.times.each do |c|
      bingo_row = false unless board[r][c].mark
      bingo_col = false unless board[c][r].mark
    end
    return true if bingo_row || bingo_col
  end
  return false
end
def sumAllUnmarkedValue(board)
  sum = 0
  board.each do |row|
    row.each  do |point|
      sum += point.value unless point.mark
    end
  end
  return sum
end
def gameFirstWin(balls, boards)
  balls.each do |ball|
    boards.each do |board|
      board.each do |row|
        row.each  do |point|
          point.mark = true if point.value == ball
        end
      end
      return sumAllUnmarkedValue(board) * ball if check(board)
    end
  end
  return nil
end
def gameLastWin(balls, boards)
  numBoards = Array.new(boards.size, false)
  balls.each do |ball|
    boards.each_with_index do |board, i|
      board.each do |row|
        row.each  do |point|
          point.mark = true if point.value == ball
        end
      end
      numBoards[i] = true if check(board)
      return sumAllUnmarkedValue(board) * ball if numBoards.all? { |b| b }
    end
  end
  return nil
end

p gameLastWin(balls, bd1)
p gameFirstWin(balls, boards)
