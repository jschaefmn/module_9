# This program demonstrates object pickling
import pickle

# main function
def main():
  again = 'y' # to control loop repetition
  
  # open a file for binary writing
  output_file = open('info.dat', 'wb')
  
  # Get data until user wants to stop
  while again.lower() == 'y':
    # get data about person and save it
    save_data(output_file)
    
    # does user want to enter more data?
    again = input('Enter more data? (y/n): ')
    
  # close the file
  output_file.close()

# The save_data function gets data about person,
# stores it in a dictionary, and then pickles the
# dictionary to the specified file
def save_data(file):
  # create an empty dictionary
  person = {}
  
  # get data for a person and store 
  # it in the dictionary
  person['name'] = input('Name: ')
  person['age'] = input('Age: ')
  person['weight'] = float(input('Weight: '))
  
  # Pickle the dictionary
  pickle.dump(person, file)
  
# call main function
if __name__ == '__main__':
  main()