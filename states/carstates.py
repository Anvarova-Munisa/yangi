from aiogram.fsm.state import State, StatesGroup

class CarState(StatesGroup):
    type = State()
    car_name = State()
    color = State()
    info = State()