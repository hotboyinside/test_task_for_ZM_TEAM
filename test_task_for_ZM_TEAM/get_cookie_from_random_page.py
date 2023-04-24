import sqlite3

from selenium import webdriver
from make_requests import find_news
from random import choice
from typing import List
from setup_db import prepare_table, path_to_db
from multiprocessing import Pool
from threading import Thread


def get_cookie() -> None:
    """
    In this function we go to random news and get cookies from this page,
    after we save cookies in database
    :return: None
    """
    links: List = find_news()
    if links:
        one_link: str = choice(links)
        with webdriver.Edge() as driver:
            driver.implicitly_wait(10)
            driver.get(one_link)
            cookies = driver.get_cookies()
            with sqlite3.connect(path_to_db) as conn:
                cursor = conn.cursor()
                for index, cookie in enumerate(cookies, start=1):
                    cursor.execute("""
                        UPDATE 'Cookie Profile' SET cookie=? WHERE id=?;
                        """, (f'{cookie}', index))


def get_data_from_db(user_id: int) -> None:
    """
    Get user_id and collect data from database by this user_id
    :param user_id: Integer
    :return: None
    """
    with sqlite3.connect(path_to_db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, datetime_of_creation, cookie FROM 'Cookie Profile'
        WHERE id=?;
        """, (user_id, ))
        print(cursor.fetchone())


def get_profiles() -> None:
    """
    with multiprocessing and use 'get_data_from_db' collect profiles
    :return:
    """
    users_id = [num for num in range(1, 16)]
    with Pool(processes=3) as pool:
        pool.map(get_data_from_db, users_id)


if __name__ == "__main__":
    prepare_table()
    get_cookie()
    get_profiles()
