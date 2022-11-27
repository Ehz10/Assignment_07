#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Tiago Rodrigues, 2022-Nov-17. Updated File
# Tiago Rodrigues, 2022-Nov-27, Modified code to add binary data and error code handling
#------------------------------------------#

#TODone docstrings for every function
#TODone add error handling in functions
import pickle


# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    # TODone add functions for processing here
    @staticmethod
    def add_data(ID, Title, Artist):
        ''''
        Function to add data inside the table
        
        Args:
            ID (String): id
            Title(String): cd Title
            Artist(String): cd Artist
            
        Returns:
            lstTbl (list)
        '''
        # 3.3.2 Add item to the table
        try:
            intID = int(ID)
            dicRow = {'ID': intID, 'Title': Title, 'Artist': Artist}
            lstTbl.append(dicRow)
            return lstTbl
        except Exception as e:
            print('There was a error!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')
    
    @staticmethod
    def del_inventory():
        '''
        Function to delete data from the table
        
        Args:
            None
            
        Returns:
            None
        
        '''
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except ValueError as e:
            print('That is not an integer!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        # 3.5.2 search thru table and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'rb')
        except FileNotFoundError as e:
            print('File not found.')
            print('Build in error info:')
            print(type(e), e, e,__doc__, sep='\n')
        try: 
            data = pickle.load(objFile)
            for line in range(0, len(data)):
                table.append(data[line])
        except Exception as e:
            print('There was an error.')
            print('Build in error info:')
            print(type(e), e, e,__doc__, sep='\n')
        
        objFile.close()  
    
    @staticmethod
    def write_file(file_name, table):
        '''
        #Function to write inside the file file_name
        
        Args:
            file_name: the name of the file
            table: the table with data to insert into the file
            
        Returns:
            None
        '''
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            try:
                objFile = open(strFileName, 'wb')
            except FileExistsError as e:
                print('File not found')
                print('Build in error info:')
                print(type(e), e, e.__doc__, sep='\n')
            for row in lstTbl:
                lstValues = list(row.values())
                try:
                    lstValues[0] = str(lstValues[0])
                except Exception as e:
                    print('There was a error!')
                    print('Build in error info:')
                    print(type(e), e, e.__doc__, sep='\n')
                pickle.dump(lstTbl,objFile)
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        pass
    
    
# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODone add I/O functions as needed
    @staticmethod
    def add_iventory():
        '''
        Function that request three inputs to user to add data in table
        
        Args:
            None
            
        Returns:
            strID (String): id 
            strTitle (String): cd Title
            strArtist (String): cd Artist
        '''
        try:
        # 3.3.1 Ask user for new ID, CD Title and Artist
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
        except ValueError as e:
            print('Incorrect Character')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        return strID, strTitle, strArtist
        
        
    
# 1. When program starts, read in the currently saved Inventory
# check if the file exists before start the program
try:
    FileProcessor.read_file(strFileName, lstTbl)
except FileExistsError:
    print('The file {} doesn\'t exist!'.format(strFileName))

#FileProcessor.read_file(strFileName, lstTbl)


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODone move IO code into function
        # 3.3.2 Add item to the table
        # TODone move processing code into function
        strID, strTitle, strArtist = IO.add_iventory()
        lstTbl = DataProcessor.add_data(strID, strTitle, strArtist) 
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        DataProcessor.del_inventory()
        # 3.5.2 search thru table and delete CD
        # TODone move processing code into function       
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
         # start loop back at top.
         FileProcessor.write_file(strFileName, lstTbl)
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')