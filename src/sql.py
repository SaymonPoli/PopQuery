import psycopg

def connect (dns: str):
    try:
        conn = psycopg.connect(dns)
        return conn
    except psycopg.Error as e:
        raise RuntimeError(f"Uneable to connect to database: {e}")


def 
    
