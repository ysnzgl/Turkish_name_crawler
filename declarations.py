from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class IsimlerKadin(Base):
    __tablename__ = 'ISIMLERKADIN'

    id = Column(Integer, primary_key=True,autoincrement=True)
    Sira = Column(Integer, nullable=False)
    Aciklama = Column(String(250), nullable=False)
    KullanimSayi=Column(String(50), nullable=False)

    def Add(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        session.commit()
    
class IsimlerErkek(Base):
    __tablename__ = 'ISIMLERERKEK'

    id = Column(Integer, primary_key=True,autoincrement=True)
    Sira = Column(Integer, nullable=False)
    Aciklama = Column(String(250), nullable=False)
    KullanimSayi=Column(String(50), nullable=False)

    
    def Add(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        session.commit()
    

# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///IsimDB.db')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)