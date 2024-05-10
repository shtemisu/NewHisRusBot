from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command, StateFilter
from bs4 import BeautifulSoup
import requests
from selenium import webdriver as wd
import emoji

from keyboards import keyboards as kb
from app.states import StatesWiki, StateHist

router1 = Router()


@router1.message(Command("start", "menu"))
async def start(msg: Message):
    await msg.answer(text=f'\nПриветствую' + emoji.emojize(':waving_hand:') + f',<b>{msg.from_user.first_name}!</b>'
                                                                              '\n'
                                                                              '\nЯ — <b>бот-помощник по Истории '
                                                                              'России</b>'
                                                                              '\nЯ храню в себе все с древних, '
                                                                              'не запамятных времен!'
                                                                              '\nНу и много других вещей'
                                                                              '\nДля старта тыкни кнопочку :)'
                                                                              '\n'
                                                                              '\n<u>Developed by shtemisu</u>',
                     reply_markup=kb.inline_kb)


@router1.callback_query(F.data == "aboutUs")
async def info(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text('<b><u>Создано специально для дисциплины "История России"</u></b>'
                                     '\n'
                                     '<b>\nРазработали студенты СВФУ им М.К. Аммосова</b>'
                                     '<b>\nИнститута математики и информатики,группы ИТСС-23:</b>'
                                     '\n'
                                     '\n' + emoji.emojize('🔵') + 'Пинигин Роман — <i>главный разработчик</i>'
                                     '\n' + emoji.emojize('🔵') + 'Ефимов Тимофей — <i>генератор идей</i>'
                                     '\n' + emoji.emojize('🔵') + 'Аммосов Александр — <i>генератор идей</i>'
                                     '\n' + emoji.emojize('🔵') + 'Сыроватский Айысхан — <i>генератор идей</i>'
                                     '\n' + emoji.emojize('🔵') + 'Колодезников Еремей — <i>генератор идей</i>',
                                     parse_mode="HTML",
                                     reply_markup=kb.back_kb)


@router1.callback_query(F.data == 'search')
async def search_msg(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Выберите источник..." + emoji.emojize('👀'), reply_markup=kb.search_kb)


@router1.callback_query(F.data == 'back')
async def main_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=f'\nПриветствую' + emoji.emojize(':waving_hand:') + f',<b>{callback.from_user.first_name}!</b>'
                                                                 '\n'
                                                                 '\nЯ - <b>бот-помощник по Истории России</b>'
                                                                 '\nЯ храню в себе все с древних, не запамятных времен!'
                                                                 '\nНу и много других вещей'
                                                                 '\nДля старта тыкни кнопочку :)'
                                                                 '\n'
                                                                 '\n<u>Developed by shtemisu</u>',
        reply_markup=kb.inline_kb)
    await state.clear()


@router1.callback_query(F.data == 'wiki', StateFilter(None))
async def wiki(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Введите запрос..." + emoji.emojize('🌐'), reply_markup=kb.back_kb)
    await state.set_state(StatesWiki.wait_result)


@router1.message(StatesWiki.wait_result)
async def step(message: Message, state: FSMContext):
    file_ids = []
    await state.set_state(StatesWiki.got_result)
    text = message.text
    url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + text
    request = requests.get(url)
    s = BeautifulSoup(request.text, "html.parser")
    l = s.find_all("div", class_="mw-search-result-heading")
    if len(l) > 0:
        url = "https://ru.wikipedia.org" + l[0].find("a")["href"]
    option = wd.ChromeOptions()
    option.add_argument('headless')
    driver = wd.Chrome(option)
    driver.get(url)

    driver.execute_script("window.scrollTo(200,200)")
    driver.save_screenshot("img.png")
    driver.close()
    img = FSInputFile('img.png')
    result = await message.answer_photo(img, caption='\nСсылка на статью: ' + url, reply_markup=kb.back_kb)
    file_ids.append(result.photo[-1].file_id)
    await state.clear()


@router1.callback_query(F.data == 'hist', StateFilter(None))
async def hist(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Введите запрос..." + emoji.emojize('🌐'), reply_markup=kb.back_kb)
    await state.set_state(StateHist.wait_result)


@router1.message(StateHist.wait_result)
async def stephist(message: Message, state: FSMContext):
    file1_ids = []
    await state.set_state(StateHist.got_result)
    text = message.text
    url = "https://histrf.ru/search?q=" + text
    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')
    links = bs.find_all("div", class_="w-full max-w-[100%] sm:max-w-[50%] xl:max-w-[33.33333%] p-2.5")
    if len(links) > 0:
        url = "https://histrf.ru" + links[1].find('a')['href']
    option = wd.ChromeOptions()
    option.add_argument('headless')
    driver = wd.Chrome(option)
    driver.get(url)

    driver.execute_script("window.scrollTo(300,400)")
    driver.save_screenshot("img1.png")
    driver.close()
    img1 = FSInputFile('img1.png')
    result = await message.answer_photo(img1, caption='\nСсылка на статью: ' + url, reply_markup=kb.back_kb)
    file1_ids.append(result.photo[-1].file_id)
    await state.clear()


@router1.callback_query(F.data == 'donate')
async def donate(callback: CallbackQuery):
    await callback.message.edit_text(text="Спасибо, что хотите нас поддержать :)"
                                          "\nПока в разработке:(", reply_markup=kb.back_kb)
