require "pp"

Point = Struct.new(:value, :mark)
class Bingo
	attr_accessor :balls
	attr_accessor :boards
	def initialize
		line = gets
		@balls = line.chomp.split(",").map(&:to_i)
		@boards = []
		while 1 do
			line = gets # space
			break if line == nil
			board = []
			5.times.each do
				line = gets
        l = line.split(" ").map(&:to_i)
        row = []
        l.each do |value|
          row << Point.new(value, false)
        end
        board << row
			end
			@boards << board
		end
	end
  def pboard(board)
    board.each do |row|
      row.each do |point|
        if point.mark
          printf "\x1b[1m%3d\x1b[0m", point.value
        else
          printf "%3d", point.value
        end
      end
      puts
    end
    puts
  end
  def pboards
    @boards.each do |board|
      pboard(board)
    end
  end

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
	def gameFirstWin
		@balls.each do |ball|
			@boards.each do |board|
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
	def gameLastWin
    numBoards = Array.new(@boards.size, false)
		@balls.each do |ball|
			@boards.each_with_index do |board, i|
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

end
bingo = Bingo.new
#p bingo.balls
#bingo.pboards
#p bingo.gameFirstWin
p bingo.gameLastWin
