from engine import TicTacToe
from players import RandomComputerPlayer
from models import Mark
from renderers import ConsoleRenderer


player1 = RandomComputerPlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()