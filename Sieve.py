import pandas as pd # type: ignore
import os
import glob

def find_and_filter_csv():
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    print()
    
    print("Files in current directory:")
    files = os.listdir('.')
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file}")
    print()
    
    csv_files = glob.glob("*.csv")
    found_file = None
    
    if not found_file and csv_files:
        print("\n Available CSV files to choose from:")
        for i, csv_file in enumerate(csv_files, 1):
            print(f"  {i}. {csv_file}")
        
        try:
            choice = int(input("\nEnter the number of your CSV file: ")) - 1
            if 0 <= choice < len(csv_files):
                found_file = csv_files[choice]
                print(f"Using: {found_file}")
            else:
                print("Invalid choice")
                return
        except ValueError:
            print("Invalid input")
            return
    
    if not found_file:
        print("\n No CSV file found!")
        print(f"Current folder location: {current_dir}")
        return
    
    try:
        print(f"\n Reading file: {found_file}")
        df = pd.read_csv(found_file)
        
        print(f" File loaded successfully!")
        print(f"   Columns: {len(df)}")
        print(f"   Columns: {len(df.columns)}")
        
        print("\nAvailable columns:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i}. {col}")

        try:
            col_choice = int(input("\nSelect column by number: ")) - 1
            if 0 <= col_choice < len(df.columns):
                Column_to_filter = df.columns[col_choice]
                print(f" Using column: {Column_to_filter}")
            else:
                print(" Invalid column number.")
                return
        except ValueError:
            print(" Invalid input. Please enter a number.")
            return
        
        print(f"\n Column values:")
        counts = df[str(Column_to_filter)].value_counts()
        for i, (val, count) in enumerate(counts.items(), 1):
            print(f"{i}. {val}: {count}")
        
        filter_value = input("Enter the value to filter for: ")
        filtered_df = df[df[Column_to_filter] == filter_value]
        print(f"\n Filtering results:")
        print(f"   Original rows: {len(df)}")
        print(f"   Needed rows: {len(filtered_df)}")
        print(f"   Rows removed: {len(df) - len(filtered_df)}")
        
        nound_file = os.path.splitext(found_file)[0]
        output_filename = nound_file + " filtered" + ".csv"
        filtered_df.to_csv(output_filename, index=False)
        print(f"\nSaved filtered data to: {output_filename}")
        print()
        print("Done!")
        
    except FileNotFoundError:
        print(f"Still can't find file: {found_file}")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    find_and_filter_csv()