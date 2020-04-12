import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import hashlib
import logging
import traceback

import models.init

engine = models.init.engine()

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    username = sqlalchemy.Column(sqlalchemy.String(20))
    password = sqlalchemy.Column(sqlalchemy.String(40))
    mail_address = sqlalchemy.Column(sqlalchemy.String(20))
    address = sqlalchemy.Column(sqlalchemy.String(40))



class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)

        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()


    def make_password(self, password):
        encoded_password = password.encode('utf-8')
        hash_password = hashlib.sha256(encoded_password).hexdigest()
        return str(hash_password)

    def create_user(self, username, password,
                        mail_address, address):
        try:
            person = Person()
            person.username = username
            person.password = self.make_password(password)
            person.mail_address = mail_address
            person.address = address

            self.session.add(person)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()


    def read_database(self, id_num=None):
        try:
            persons = self.session.query(Person).all()
            all_database = []

            for person in persons:
                dict_all = {
                    'id': person.id,
                    'username': person.username,
                    'password': person.password,
                    'mail_address': person.mail_address,
                    'address': person.address
                }
                if id_num is None:
                    all_database.append(dict_all)
                    result = all_database
                else:
                    if dict_all['id'] == id_num:
                        result = dict_all
            return result
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def delete_database(self, id):
        delete_content = self.session.query(Person).filter_by(id=id).first()
        self.session.delete(delete_content)
        self.session.commit()

    def check_user(self, username, password):
        r_db = self.read_database()
        encode_ps = password.encode('utf-8')
        hash_password = hashlib.sha256(encode_ps).hexdigest()

        for i in range(len(r_db)):
            if r_db[i]['username'] == username and r_db[i]['password'] == hash_password:
                return True
                break
            if i == len(r_db) - 1:
                return False
                break


if __name__ == '__main__':
    op = UserOperation()

    print(op.check_user('root', 'root'))