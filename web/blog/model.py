import web, datetime

db = web.database(dbn='mysql' , db='test' ,user='bin' , pw ='bin')

def get_posts():
    return db.select('entries',order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id' ,vars=locals())[0]
    except IndexError:
        return None
    

def new_post(title, text):
    db.insert('entries' , title=title, content = text , posted_on = 'sysdate' )
    

def del_post(id):
    db.delete('entries' , where = 'id=$id' , vars=locals())
    

def update_post(id, title, text):
    db.update('entries' , where = "id=$id" ,vars=locals() ,title=title , content=text)