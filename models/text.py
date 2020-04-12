import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

import logging

import models.init

engine = models.init.engine()

Base = sqlalchemy.ext.declarative.declarative_base()

class Text(Base):
    __tablename__ = 'text'

    number = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True
    )
    username = sqlalchemy.Column(sqlalchemy.String(20))
    text = sqlalchemy.Column(sqlalchemy.String(200))
    page_id = sqlalchemy.Column(sqlalchemy.Integer())

class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = Session()

    def create_text(self, username, text, page_id):
        try:
            text_op = Text()

            text_op.username = username
            text_op.text = text
            text_op.page_id = page_id

            self.session.add(text_op)
            self.session.commit()
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def read_text(self, id_num=None):
        try:
            texts = self.session.query(Text).all()
            all_database = []
            result_dict = {}

            for text in texts:
                dict_all = {
                    'username': text.username,
                    'text': text.text,
                    'page_id': text.page_id,
                }
                all_database.append(dict_all)

            for i in range(len(all_database)):
                result_dict[i] = all_database[i]
            result = result_dict

            if id_num is None:
                return result
            return result[id_num]
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def read_page_id(self, page_id):
        try:
            texts = self.session.query(Text).all()
            page_id_in_database = []

            for text in texts:
                if page_id == text.page_id:
                    dict_all = {
                        'username': text.username,
                        'text': text.text,
                        'page_id': text.page_id,
                    }
                    page_id_in_database.append(dict_all)
            result = page_id_in_database

        except:
            logging.error('fail')
        finally:
            self.session.close()
        return result

if __name__ == '__main__':
    op = UserOperation()

    print(op.read_page_id(2))












