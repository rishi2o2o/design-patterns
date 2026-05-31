from abc import ABC, abstractmethod

# --- Abstract Class setting up the skeleton ---
class DataParser(ABC):

    # The Template Method defines the exact sequence of steps
    def parse_data_file(self) -> None:
        self._open_file()
        self.extract_data()
        self.parse_data()
        self.close_file()

    # Common behavior implemented in the base class
    def _open_file(self) -> None:
        print("Opening the data file...")

    def close_file(self) -> None:
        print("Closing the data file safely.\n")

    # Abstract steps to be implemented by child classes
    @abstractmethod
    def extract_data(self) -> None:
        pass

    @abstractmethod
    def parse_data(self) -> None:
        pass


# --- Concrete Subclass for CSV files ---
class CSVParser(DataParser):
    
    def extract_data(self) -> None:
        print("Extracting raw rows from CSV.")

    def parse_data(self) -> None:
        print("Parsing comma-separated text into Python dictionaries.")


# --- Concrete Subclass for JSON files ---
class JSONParser(DataParser):
    
    def extract_data(self) -> None:
        print("Extracting raw key-value hierarchies from JSON.")

    def parse_data(self) -> None:
        print("Parsing JSON tokens into Python dictionaries.")


# --- Client Code ---
if __name__ == "__main__":
    
    print("--- Processing CSV ---")
    csv_processor = CSVParser()
    csv_processor.parse_data_file()

    print("--- Processing JSON ---")
    json_processor = JSONParser()
    json_processor.parse_data_file()

