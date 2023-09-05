from datetime import date

from config import PGSettings
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

pg = PGSettings()
engine = create_engine(
    f"postgresql+psycopg2://{pg.user}:{pg.password}@{pg.host}:{pg.port}/{pg.dbname}"
)

Base.prepare(autoload_with=engine)

session = Session(engine)

ParsingData = Base.classes.parsing_data


def get_max_date() -> date:
    """Last date written in the table

    Returns:
        date: Last date written in the table
    """
    max_date = session.query(func.max(ParsingData.dt)).first()[0]
    return max_date


def get_recent_parsing() -> list[ParsingData]:
    """Returns most recent parsing results

    Returns:
        list[ParsingData]: Most recent parsing results
    """
    recent_data = (
        session.query(ParsingData).where(ParsingData.dt == get_max_date()).all()
    )
    return recent_data
