from sqlalchemy.orm import Session
from sqlalchemy import select, Row, Tuple, Sequence
from db.engine import engine
from entities.place import Place

def get_places_by_floor(floor: int):
    with Session(engine) as session:
        query = select(Place).filter_by(floor=floor)
        result = session.execute(query).all()
        return [row.Place for row in result]
        