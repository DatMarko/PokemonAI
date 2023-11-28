
import openpyxl


#########################################################
# POKEMON DATABASES
#########################################################
moves_path = "Pokemon_Moves.xlsx"
moves_wb_obj = openpyxl.load_workbook(moves_path)
pokemon_path = "Pokemon_Dex.xlsx"
pokemon_wb_obj = openpyxl.load_workbook(pokemon_path)

# Get workbook active sheet object 
# from the active attribute 
moves_sheet_obj = moves_wb_obj.active 
pokemon_sheet_obj = pokemon_wb_obj.active
  
#selects the rows (move)
moves_row_obj = moves_sheet_obj[15]

#selects column of selected row (details of move)
current_move = moves_row_obj
#print("Current move is: " + current_move[1].value)

#########################################################
# CREATION OF OBJECTS
#########################################################
class Pokemon:
      def __init__(self, pokemon, move1, move2, move3, move4):
        self.pokemon = pokemon
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4



def damage(pokemon1, pokemon2, move):
    #print("Pokemon: " + pokemon1.name)
    #print("Move: " + pokemon1.move.name)
    #print(pokemon1.name + "'s HP: " + str(pokemon1.hp_stat))
    print(pokemon1[1].value + "'s HP before damage: " + str(pokemon1[14].value))
    print(pokemon2[1].value + " used " + move[1].value + "!")
    print(move[6].value)
    damage = int(move[6].value)
    #print("Damage to: " + pokemon1.name + " | Damge taken = " + str(pokemon2.move.power))
    
    new_hp = pokemon1[14].value - damage
    print(pokemon1[1].value + "'s HP after damage: " + str(new_hp))

    return new_hp

#########################################################
# CREATION OF POKEMON AND MOVES
#########################################################

def create_pokemon(name, move1, move2, move3, move4):
  lst = []
  for i in pokemon_sheet_obj:
    temp_lst = []
    if i[1].value == name:
      temp_lst.append(i)
      temp_lst.append(move1)
      temp_lst.append(move2)
      temp_lst.append(move3)
      temp_lst.append(move4)
      print(i[1].value)
      lst = temp_lst
      break
  #new_pokemon = Pokemon()
  
  return lst


#########################################################
# START USING FUNCTIONS
#########################################################

#test of creating a pokemon with a moveset
mew = create_pokemon('Mew', moves_sheet_obj[400], moves_sheet_obj[100], moves_sheet_obj[3], moves_sheet_obj[500])
print(str(mew[0][1].value) + "'s known moves are: " + str(mew[1][1].value) + ", " + str(mew[2][1].value) + ", " + str(mew[3][1].value) + ", " + str(mew[4][1].value))

bulbasaur = pokemon_sheet_obj[3]
mew = pokemon_sheet_obj[153]
air_cutter = moves_sheet_obj[15]

#test of the damage calculation
new_hp = damage(bulbasaur, mew, air_cutter)


