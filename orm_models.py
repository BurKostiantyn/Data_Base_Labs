from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from config import db_config

Base = declarative_base()

DSN = f"postgresql+psycopg://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

engine = create_engine(DSN, echo=False)
Session = sessionmaker(bind=engine)


# --- ОПИС КЛАСІВ (Таблиць) ---

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    documents = relationship("Document", back_populates="category", passive_deletes=True)

    def __repr__(self):
        return f"({self.category_id}) {self.name}: {self.description}"


class Document(Base):
    __tablename__ = 'documents'

    document_id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content_path = Column(String(255), default='default/path')
    created_at = Column(Date)

    category_id = Column(Integer, ForeignKey('categories.category_id'), nullable=False)

    category = relationship("Category", back_populates="documents")

    def __repr__(self):
        return f"Doc(id={self.document_id}, title='{self.title}', cat_id={self.category_id})"