def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  # не работает


inner_function()  #ошибка

test_function()  # это работает
