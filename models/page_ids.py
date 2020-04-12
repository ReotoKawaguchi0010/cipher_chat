import traceback
import logging

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

import models.init

engine = models.init.engine()

Base = sqlalchemy.ext.declarative.declarative_base()


class PageId(Base):
    __tablename__ = 'page_id'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    page_title = sqlalchemy.Column(sqlalchemy.String(20))

class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)

        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()


    def create_page(self, page_title):
        if self.read_database():
            try:
                if self.key_title(page_title):
                    return logging.error('already title name')
            except:
                print('success')
        try:
            page_id = PageId()
            page_id.page_title = page_title

            self.session.add(page_id)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_database(self, id_num=None):
        try:
            page_ids = self.session.query(PageId).all()
            all_database = []

            if not page_ids:
                return None

            for page_id in page_ids:
                dict_all = {
                    'id': page_id.id,
                    "page_title": page_id.page_title
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

    def key_title(self, search_value):
        in_database = self.read_database()
        for i in range(len(in_database)):
            key_title = {in_database[i]['page_title']: in_database[i]['id']}
            if search_value == in_database[i]['page_title']:
                break
        return key_title[search_value]

    def id_title(self, search_id):
        search_id = int(search_id)
        in_database = self.read_database()
        for i in range(len(in_database)):
            key_title = {in_database[i]['id']: in_database[i]['page_title']}
            if search_id == in_database[i]['id']:
                break
        return key_title[search_id]



if __name__ == '__main__':
    op = UserOperation()

    op.create_page('reoto')

    print(op.key_title('test'))
    print(op.id_title('2'))
