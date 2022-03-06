class Utils():

    @staticmethod
    def check_border_coordinates(y,x):
        '''
        This function checks the coordinates of the border and returns if border is present or not
        '''
        if y == 0 or y == 40:
            return True
        elif x == 0 or x == 79:
            return True
        else:
            return False
