import  sqlite3

class SQLighter:
    def __init__(self, database_file):
        """Подключение к БД и сохранение курсора соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

                    ##############################
                    ###########ДОБАВИТЬ###########
                    ##############################
    def add_user_admin(self, user, id):
        """Добавление нового пользователя USER"""
        with self.connection:
            return self.cursor.execute("UPDATE `admin_panel` SET `user` = ? WHERE `id` = ?", (user, id))
    def add_status_admin(self, id):
        """Добавление нового id и статус ЗАКАЗЧИКА USER"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `admin_panel` (id, status) VALUES (?, 'CUST')", (id,))
    def add_id_admin(self, id):
        """Добавление нового id USER"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `admin_panel` (id) VALUES (?)", (id,))
    def add_map_admin(self, map):
        """Добавление новой карты"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `map` (map) VALUES (?)", (map,))

                    ##############################
                    ###########ПРОВЕРКА###########
                    ##############################
    def selekt_id_admin(self, user_id):
        """Провенрка есть ли пользователь в базе USER"""
        with self.connection:
            return self.cursor.execute("SELECT `id` FROM `admin_panel` WHERE `id` = ?", (user_id,)).fetchall()
    def liset_USER_admin(self):
        """Провенрка ВСЕ в базе USER"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `admin_panel` WHERE `status` = 'PROM'").fetchall()
    def liset_CUST_admin(self):
        """Провенрка ВСЕ в базе USER"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `admin_panel` WHERE `status` = 'CUST'").fetchall()
    def liset_MAP_admin(self, id):
        """Провенрка ВСЕ в базе USER"""
        with self.connection:
            return self.cursor.execute("SELECT `map`, `customer` FROM `prom` WHERE `user_id` = ?", (id,)).fetchall()
    def selekt_map_admin(self, map):
        """Провенрка наличия карты в базе"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `map` WHERE `map` = ?", (map,)).fetchall()
    def selekt_map_pad_admin(self, map):
        """Провенрка наличия карты в базе"""
        with self.connection:
            return self.cursor.execute("SELECT `pad` FROM `map` WHERE `map` = ?", (map,)).fetchall()
    def selekt_adres_id_admin(self, id, map):
        """Провенрка адреса у пользователя inline"""
        with self.connection:
            return self.cursor.execute("SELECT `adres` FROM `prom` WHERE `user_id` = ? AND `map` = ?", (id, map,)).fetchall()
    def selekt_status_admin(self, ststus, id):
        """Провенрка ВСЕ в базе USER"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `admin_panel` WHERE `status` = ? AND `id` = ?", (ststus, id,)).fetchall()
    def selekt_photo_admin(self, adres):
        """Провенрка фото и подъезд по адресу"""
        with self.connection:
            return self.cursor.execute("SELECT `photo`, `pad` FROM `prom` WHERE `adres` = ?", (adres,)).fetchall()
    def selekt_all_admin(self, id, map):
        """Провенрка фото и подъезд по адресу"""
        with self.connection:
            return self.cursor.execute("SELECT `photo`, `adres`, `pad` FROM `prom` WHERE `user_id` = ? AND `map` = ?", (id, map)).fetchall()




                    ##############################
                    ###########УДАЛИТЬ############
                    ##############################
    def delete_all(self, user_id, photo):
        with self.connection:
            return self.cursor.execute("DELETE FROM `prom` WHERE `user_id` = ? AND `photo` = ?", (user_id, photo,))

    def close(self):
        """Закрытие соединения"""
        self.connection.close()