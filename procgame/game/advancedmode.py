from ..game import Mode

class AdvancedMode(Mode):
    """Abstraction of a game mode to be subclassed by the game
    programmer.    
    """    
    System  = 0  # added on reset, removed/readded on reset, removed never
    Ball    = 1  # added on ball start, removed on ball end
    Game    = 2  # added on game start, removed on game end
    Manual  = 3  # programmer must add/remove mode

    def __init__(self, game, priority, mode_type=Manual):
        """
        this
        """
        super(AdvancedMode, self).__init__(game, priority)
        self.mode_type = mode_type
        self.mode_init()

        game.notifyOfNewMode(self)

    def mode_init(self):
        """ called when this mode is created 
            --use to set up initial vars as needed 
        """
        pass

    def force_event_next(self):
        self.game.notifyNextModeNow(self)