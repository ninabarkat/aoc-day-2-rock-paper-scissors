class InputController:
    file_path = './input/input.txt'

    def __init__(self):
        print('Initialising InputController class.')

    def get_marray(self):
        return open(self.file_path).read().splitlines()
