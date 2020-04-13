import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

import logging

import models.init

engine = models.init.engine()

Base = sqlalchemy.ext.declarative.declarative_base()

class JapaneseText(Base):
    __tablename__ = 'japanese_text'

    number = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True
    )
    japanese_text = sqlalchemy.Column(sqlalchemy.String(20))
    text = sqlalchemy.Column(sqlalchemy.String(200))
    page_id = sqlalchemy.Column(sqlalchemy.Integer())

class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = Session()

    def create_text(self, japanese_text, text, page_id):
        try:
            text_op = JapaneseText()

            text_op.japanese_text = japanese_text
            text_op.text = text
            text_op.page_id = page_id

            self.session.add(text_op)
            self.session.commit()
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def read_text(self, decode_letter):
        try:
            texts = self.session.query(JapaneseText).all()
            all_database = []

            for text in texts:
                dict_all = {
                    'japanese_text': text.japanese_text,
                    'text': text.text,
                    'page_id': text.page_id,
                }
                all_database.append(dict_all)

            for i in range(len(all_database)):
                if decode_letter == all_database[i]['text']:
                    result = all_database[i]
                    break

            return result

        except:
            logging.error('fail')
        finally:
            self.session.close()

if __name__ == '__main__':
    op = UserOperation()

    op.create_text('ファファファ', 'test', 2)

    print(op.read_text('test'))
