

class AppState:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @classmethod
    def get_app_state(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    

def show_singleton():
    from os.path import basename
    print()
    print(f"{basename(__file__):_^80}")

    app_state1 = AppState.get_app_state()
    print(app_state1.is_logged_in, id(app_state1))

    app_state2 = AppState.get_app_state()
    print(app_state2.is_logged_in, id(app_state2))

    app_state1.is_logged_in = True

    print(app_state2.is_logged_in, id(app_state2))
