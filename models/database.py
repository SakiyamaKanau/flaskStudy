import psycopg2


import psycopg2

def connect_to_database():
    return psycopg2.connect(
        "postgres://neon:Ehgk5s2OvUKm@ep-late-forest-07793227.us-east-2.aws.neon.tech/neondb?sslmode=require&options=project%3Dep-late-forest-07793227"
    )