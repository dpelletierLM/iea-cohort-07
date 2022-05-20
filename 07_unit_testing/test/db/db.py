import os

def get_databas_host():
    host = os.getenv("DATABASE_HOST")
    if not host: # Returns false if host is None or ''
        return None
    return "mysql://" = host

if __name__ == "__main__":
    print(get_databas_hostbase_host())
