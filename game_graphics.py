main_menu = """+=============================================================================+
     ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
     ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
     ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                         (Survival ASCII Strategy Game)
+=============================================================================+

[New] Game
[Load] Game
[High] Scores
[Help]
[Exit]"""


play_menu = """__________(LOG)__________________________________________________(LOG)__________
+==============================================================================+


                                 (ROBOT IMAGES)


+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+"""


play_menu_rt = """+==============================================================================+
  $   $$$$$$$   $  |  $   $$$$$$$   $  |  $   $$$$$$$   $
  $$$$$     $$$$$  |  $$$$$     $$$$$  |  $$$$$     $$$$$
      $$$$$$$      |      $$$$$$$      |      $$$$$$$
     $$$   $$$     |     $$$   $$$     |     $$$   $$$
     $       $     |     $       $     |     $       $
+==============================================================================+
| Titanium: 0                                                                  |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+"""


upgrade_menu = """
                       |================================|
                       |          UPGRADE STORE         |
                       |                         Price  |
                       | [1] Titanium Scan         250  |
                       | [2] Enemy Encounter Scan  500  |
                       | [3] New Robot            1000  |
                       |                                |
                       | [Back]                         |
                       |================================|
"""


save_game = """
                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|"""


load_game = """
                        |==============================|
                        |    GAME LOADED SUCCESSFULLY  |
                        |==============================|"""

game_over = """
                        |==============================|
                        |          GAME OVER!          |
                        |==============================|
                        """


robot_graphic = """  $   $$$$$$$   $  
  $$$$$     $$$$$  
      $$$$$$$      
     $$$   $$$     
     $       $     """


inside_play_menu = """
                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|"""

def main():
    print(play_menu, main_menu, robot_graphic, inside_play_menu,play_menu_rt, load_game, save_game,
          play_menu_rt, sep="\n\n\n")

if __name__ == "__main__":
    main()