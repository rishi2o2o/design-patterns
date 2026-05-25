class DatabaseConnection:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("creating new db conn instance...")
            cls._instance = cls()
        return cls._instance

if __name__ == "__main__":
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()


