import  sqlite3

class SQLighter:

    def __init__(self, database_fule):
        """Подключение к БД и сохранение курсора соединения"""
        self.connection = sqlite3.connect(database_fule)
        self.cursor = self.connection.cursor()

                    ##############################
                    ###########ДОБАВИТЬ###########
                    ##############################
    def add_user_id(self, user_id, user_name, pad, map):
        """Добавление нового id пользователя и подъезд"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `prom` (user_id, user_name, pad, map) VALUES (?,?,?,?)", (user_id, user_name, pad, map,))
    def add_adres(self, user_id, adres, adres_null, map):
        """Добавление нового адреса"""
        with self.connection:
            return self.cursor.execute("UPDATE `prom` SET `adres` = ? WHERE `user_id` = ? AND `adres` = ? AND `map` = ?", (adres, user_id, adres_null, map,))
    def add_pad(self, user_id, pad):
        """Добавление нового подъезда"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `prom` (`user_id`, `pad`) VALUES (?,?)", (user_id, pad,))
    def add_pad_map(self, pad, map):
        """Добавление нового подъезда"""
        with self.connection:
            return self.cursor.execute("UPDATE `map` SET `pad` = ? WHERE `map` = ?", (pad, map,))
    def add_photo(self, user_id, photo, photo_null, adres, data, map):
        """Добавление нового фото"""
        with self.connection:
            return self.cursor.execute("UPDATE `prom` SET `photo` = ?, `Data` = ? WHERE `user_id` = ? AND `adres` = ? AND `photo` = ? AND `map` = ?", (photo, data, user_id, adres, photo_null, map,))

                    ##############################
                    ###########ПРОВЕРКА###########
                    ##############################
    def exists_user_id(self, user_id):
        """Провенрка есть ли пользователь в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
    def exists_pad(self, user_id, pad, adres):
        """Провенрка есть ли подъезд у id"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `user_id` = ? AND `pad` = ? AND `adres` = ?", (user_id, pad, adres,)).fetchall()
            return bool(len(result))
    def exists_adres(self, user_id, adres):
        """Провенрка есть ли адрес у id"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `user_id` = ? AND `adres` = ?", (user_id, adres,)).fetchall()
            return bool(len(result))
    def exists_all(self, user_id, pad, adres, photo):
        """Провенрка есть ли подъезд у id"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `user_id` = ? AND `pad` = ? AND `adres` = ? AND `photo` = ?", (user_id, pad, adres, photo,)).fetchall()
            return bool(len(result))
    def exists_null(self, user_id, photo):
        """Провенрка есть ли подъезд без фото"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `user_id` = ? AND `photo` = ?", (user_id, photo,)).fetchall()
            return bool(len(result))
    def exists_map(self, map):
        """Провенрка есть ли карта"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `prom` WHERE `map` = ?", (map,)).fetchall()
            return bool(len(result))
    def admin_exists_map(self, map):
        """Провенрка есть ли карта"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `map` WHERE `map` = ?", (map,)).fetchall()
            return bool(len(result))

                    ##############################
                    ###########ОБНОВИТЬ###########
                    ##############################
    def update_id_pad(self, user_id, pad, photo):
        """Обновить № подъезда у id"""
        with self.connection:
            return self.cursor.execute("UPDATE `prom` SET `pad` = ? WHERE `user_id` = ? AND `photo` = ?", (pad, user_id, photo,))

                    ##############################
                    ###########УДАЛИТЬ############
                    ##############################
    def delete_all(self, user_id, photo):
        with self.connection:
            return self.cursor.execute("DELETE FROM `prom` WHERE `user_id` = ? AND `photo` = ?", (user_id, photo,))




    def close(self):
        """Закрытие соединения"""
        self.connection.close()