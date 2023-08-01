from sqlalchemy import create_engine, text

engine = create_engine("postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test")

with engine.connect() as connection:
    query = text("""
        SELECT o.first_name, o.last_name, p.name
        FROM owners o
        JOIN ponies p ON (o.id = p.owner_id);
    """)
    result = connection.execute(query)

    for row in result:
        print(row.first_name, row.last_name, "owns", row.name)

engine.dispose()