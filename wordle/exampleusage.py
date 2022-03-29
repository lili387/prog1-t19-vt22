import SwedishWordle

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

guess1 = game.Guess('mössa')
print(f'Den första gissningen var \"mössa\". Det resulterade i {guess1}. En siffra för varje bokstav i gissningen. 2 är rätt bokstav på rätt plats, 1 bokstaven finns i ordet, 0 bokstaven finns ej med i ordet. ')

guess2 = game.Guess('skylt')
print(f'Den andra gissningen var \"skylt\". Det resulterade i {guess2}.')

print(f'Den har gjort {game.num_guesses} stycken gissningar.')

# det går att starta ett nytt game med, om man så vill, ny ord längd
game.Start_new_game(10)
print(f'Den har gjort {game.num_guesses} stycken gissningar.')

guess3 = game.Guess('överträffa')
print(f'Den första gissningen i andra gamet var \"överträffa\". Det resulterade i {guess3}.')

# det går att hämta och alla ord som är 10 tecken långa
print(f'Det finns {len(game.words_in_game)} ord som är 10 bokstäver. Några av dom är {game.words_in_game[0:14]}')

# det är viktigt att man gissar ett riktigt ord som finns i listan och är rätt längd annars ger spelet ett exception
game.Guess('läderlappen')


def f(w):
    return 'm' in w and 'l' in w and w[1] == 'a' and not w[4] == 'a' and not w[4] == 'l' and not w[4] == 'm'

print(list(filter(f, game.words_in_game)))

game.Start_new_game(9)
for w in game.words_in_game:
    r = game.Guess(w)
    if not 0 in r and not 1 in r:
        print (w)