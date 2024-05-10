from aiogram.fsm.state import StatesGroup, State


class StatesWiki(StatesGroup):
    wait_result = State()
    got_result = State()


class StateHist(StatesGroup):
    wait_result = State()
    got_result = State()
