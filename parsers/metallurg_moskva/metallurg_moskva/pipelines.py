from contextlib import contextmanager

import psycopg2
from metallurg_moskva.config import Settings
from psycopg2.extras import DictCursor, execute_values


class PGPipeline:
    @contextmanager
    def __conn_context(self):
        """PostgreSQL connection context manager."""
        conn = psycopg2.connect(**Settings().pg.dict(), cursor_factory=DictCursor)
        psycopg2.extras.register_uuid()
        yield conn
        conn.close()

    def __init__(self):
        with self.__conn_context() as conn:
            curs = conn.cursor()
            curs.execute(
                """
                CREATE TABLE IF NOT EXISTS parsing_data(
                    id serial primary key,
                    name text,
                    measurement text,
                    price int,
                    diameter text,
                    brand text,
                    thickness text,
                    shelf text,
                    length text,
                    size text,
                    width int,
                    wall text,
                    dt date
                )
                """
            )
            conn.commit()

    def process_item(self, item, spider):
        with self.__conn_context() as conn:
            curs = conn.cursor()
            execute_values(
                curs,
                """insert into parsing_data (
                    name, measurement, price, diameter, brand, thickness, shelf, length, size, width, wall, dt
                ) values %s""",
                [
                    [
                        item.name,
                        item.measurement,
                        item.price,
                        item.diameter,
                        item.brand,
                        item.thickness,
                        item.shelf,
                        item.length,
                        item.size,
                        item.width,
                        item.wall,
                        item.dt,
                    ]
                ],
            )
            conn.commit()
            return item
