'''
* Lab 3 - SDEV 300 Building Secure Python Applications
* Python CLI providing users ability to search and display US
* State Capital, population, and flowers
*
* @author Christopher Stoner
'''

import matplotlib.pyplot as plt
import matplotlib.image as img


class State:
    """This is the class going to be used for our dictionary, where the key is state.name,
    which will reference the entire object it's connected to.
    Once we call upon the object from the dictionary, viewing or editing the data
    should be straight forward with methods in the state object to view and set new data

    Returns:
        State
    """

    # Constructor
    def __init__(self, name, capital, population, flower, img_flowers_path):
        """Values to be applied and associated with every state object

        Args:
            name (String): full name of the state
            capital (String): full name of the capital of the state
            population (int): population of the state
            flower (String): flower of the state
            img_flowers_path (String): Path to img in order to
            render the state flower with matplotlib
        """
        self.name = name
        self.capital = capital
        self.population = population
        self.flower = flower
        self.img_flowers_path = img_flowers_path

    # String Description of object
    def __str__(self):
        """String to print when print function called upon
        Displays name, capital, population, and flower

        Returns:
            String: formatted string to display data about object
        """
        return f"-------------------------\nState Name: {self.name}\nState Capital:" + \
            f"{self.capital}\nState Population: {self.population:,}\nState Flower: {self.flower}\n"

    def set_population(self, population):
        """allows the population value to be set by the user

        Args:
            population (int): the new population supplied by the user
        """
        self.population = population

    def render_flower_img(self):
        """Render the flower img associated with the state using img_flowers_path
        """
        im_img = img.imread(self.img_flowers_path)
        plt.imshow(im_img)
        plt.show()

    def __lt__(self, other):
        """This will allow State class to compare population size
        between different instances of State. This is needed to get
        the top 5 populations for option 3 in CLI

        Args:
            other (State): The other instance of State we wish to compare populations to

        Returns:
            bool: detects if we're comparing two of the same classes but different instances,
            then, compares the population attribute of each.
        """
        return isinstance(other, State) and self.population < other.population


def initialize_state_dictionary():
    """Dictionary containing all US states as keys to state objects
    giving more information about the state

    Returns:
        Dictionary: Dictionary of all 50 states with the keys as the state's full name,
        points to object reference for each state.
    """
    alabama = State("Alabama", "Montgomery", 4_918_689,
                    "Camellia", "./img_flowers/alabama_camellia.jpg")
    alaska = State("Alaska", "Juneau", 727_951, "Forget Me Not",
                   "./img_flowers/alaska_forget-me-not.jpg")
    arizona = State("Arizona", "Phoenix", 7_279_000,
                    "Saguaro Cactus Blossom", "./img_flowers/arizona_saguaro.jpg")
    arkansas = State("Arkansas", "Little Rock", 3_025_875,
                     "Apple Blossom", "./img_flowers/arkansas_apple-blossom.jpg")
    california = State("California", "Sacramento",
                       39_562_858, "California Poppy", "./img_flowers/california_cali-poppy.jpg")
    colorado = State("Colorado", "Denver", 5_826_185,
                     "White and Lavender Columbine", "./img_flowers/colorado_columbine.jpg")
    connecticut = State("Connecticut", "Hartford",
                        3_559_054, "Mountain Laurel", "./img_flowers/connecticut_laurel.jpg")
    delaware = State("Delaware", "Dover", 982_049, "Peach Blossom",
                     "./img_flowers/delaware_peach-blossom.jpg")
    florida = State("Florida", "Tallahassee", 21_711_157,
                    "Orange Blossom", "./img_flowers/florida_orange-blossom.jpg")
    georgia = State("Georgia", "Atlanta", 10_726_715,
                    "Cherokee Rose", "./img_flowers/georgia_cherokee-rose.jpg")
    hawaii = State("Hawaii", "Honolulu", 1_411_151, "Hibiscus",
                   "./img_flowers/hawaii_yellow-hibiscus.jpg")
    idaho = State("Idaho", "Boise", 1_823_594, "Syringa",
                  "./img_flowers/idaho_syringa.jpg")
    illinois = State("Illinois", "Springfield", 12_620_571,
                     "Purple Violet", "./img_flowers/illinois_violet.jpg")
    indiana = State("Indiana", "Indianapolis", 6_768_941,
                    "Peony", "./img_flowers/indiana_peony.jpg")
    iowa = State("Iowa", "Des Moines", 3_161_522,
                 "Wild Prairie Rose", "./img_flowers/iowa_wildrose.jpg")
    kansas = State("Kansas", "Topeka", 2_915_269, "Sunflower",
                   "./img_flowers/kansas_sunflower.jpg")
    kentucky = State("Kentucky", "Frankfort", 4_474_193,
                     "Goldenrod", "./img_flowers/kentucky_goldenrod.jpg")
    louisiana = State("Louisiana", "Baton Rouge", 4_637_898,
                      "Magnolia", "./img_flowers/louisiana_magnolia.jpg")
    maine = State("Maine", "Augusta", 1_349_367,
                  "White Pine Cone and Tassel", "./img_flowers/maine_whitepine.jpg")
    maryland = State("Maryland", "Annapolis", 6_055_558,
                     "Black-Eyed Susan", "./img_flowers/maryland_black-eyed-susan.jpg")
    massachusetts = State("Massachusetts", "Boston", 6_902_371,
                          "Mayflower", "./img_flowers/massachusetts_mayflower.jpg")
    michigan = State("Michigan", "Lansing", 9_989_642,
                     "Apple Blossom", "./img_flowers/michigan_apple-blossom.jpg")
    minnesota = State("Minnesota", "Saint Paul", 5_673_015,
                      "Pink and White Lady Slipper", "./img_flowers/minnesota_lady-slipper.jpg")
    mississippi = State("Mississippi", "Jackson", 2_971_278,
                        "Magnolia", "./img_flowers/mississippi_magnolia.jpg")
    missouri = State("Missouri", "Jefferson City",
                     6_153_233, "White Hawthorn Blossom",
                     "./img_flowers/missouri_white-hawthorn.jpg")
    montana = State("Montana", "Helena", 1_076_891, "Bitterroot",
                    "./img_flowers/montana_bitterroot.jpg")
    nebraska = State("Nebraska", "Lincoln", 1_943_202,
                     "Goldenrod", "./img_flowers/nebraska_goldenrod.jpg")
    nevada = State("Nevada", "Carson City", 3_132_971,
                   "Sagebrush", "./img_flowers/nevada_sagebrush.jpg")
    new_hampshire = State("New Hampshire", "Concord",
                          1_365_957, "Purple Lilac", "./img_flowers/new-hampshire_purple-lilac.jpg")
    new_jersey = State("New Jersey", "Trenton", 8_878_355,
                       "Violet", "./img_flowers/new-jersey_violet.jpg")
    new_mexico = State("New Mexico", "Santa Fe", 2_100_917,
                       "Yucca Flower", "./img_flowers/new-mexico_yucca.jpg")
    new_york = State("New York", "Albany", 19_376_771, "Rose",
                     "./img_flowers/new-york_rose.jpg")
    north_carolina = State("North Carolina", "Raleigh", 10_594_553,
                           "Dogwood", "./img_flowers/north-carolina_dogwood.jpg")
    ohio = State("Ohio", "Columbus", 11_701_859, "Scarlet Carnation",
                 "./img_flowers/ohio_scarlet-carnation.jpg")
    oklahoma = State("Oklahoma", "Oklahoma City", 3_973_707,
                     "Mistletoe", "./img_flowers/oklahoma_mistletoe.jpg")
    oregon = State("Oregon", "Salem", 4_253_588, "Oregon Grape",
                   "./img_flowers/oregon_oregon-grape.jpg")
    pennsylvania = State("Pennsylvania", "Harrisburg",
                         12_803_056, "Mountain Laurel",
                         "./img_flowers/pennsylvania_mountain-laurel.jpg")
    rhode_island = State("Rhode Island", "Providence", 	1_060_435,
                         "Violet",
                         "./img_flowers/rhode-island_violet.jpg")
    south_carolina = State("South Carolina", "Columbia",
                           5_213_272, "Yellow Jessamine",
                           "img_flowers/south-carolina_yellow-jessamine.jpg")
    north_dakota = State("North Dakota", "Bismarck",
                         766_044, "Wild Prairie Rose",
                         "./img_flowers/north-dakota_wild-prairie-rose.jpg")
    south_dakota = State("South Dakota", "Pierre", 	890_620,
                         "Pasque Flower", "./img_flowers/south-dakota_pasque.jpg")
    tennessee = State("Tennessee", "Nashville", 6_886_717,
                      "Iris", "./img_flowers/tennessee_iris.jpg")
    texas = State("Texas", "Austin", 29_363_096, "Bluebonnet",
                  "./img_flowers/texas_bluebonnet.jpg")
    utah = State("Utah", "Salt Lake City", 	3_258_366,
                 "Sego Lily", "./img_flowers/utah_sego-lily.jpg")
    vermont = State("Vermont", "Montpelier", 623_620,
                    "Red Clover", "/img_flowers/vermont_red-clover.jpg")
    virginia = State("Virginia", "Richmond", 8_569_752,
                     "Dogwood", "./img_flowers/virgina_dogwood.jpg")
    washington = State("Washington", "Olympia", 7_705_917, "Pink Rhododendron",
                       "./img_flowers/washington_pink-rhododendron.jpg")
    west_virginia = State("West Virginia", "Charleston",
                          1_780_003, "Rhododendron", "./img_flowers/west-virginia_rhododendron.jpg")
    wisconsin = State("Wisconsin", "Madison", 5_837_462,
                      "Wood Violet", "./img_flowers/wisconsin_wood-violet.jpg")
    wyoming = State("Wyoming", "Cheyenne", 	579_917, "Indian Paintbrush",
                    "./img_flowers/wyoming_indian-paintbrush.jpg")

    state_dic = {alabama.name: alabama,
                 alaska.name: alaska,
                 arizona.name: arizona,
                 arkansas.name: arkansas,
                 california.name: california,
                 colorado.name: colorado,
                 connecticut.name: connecticut,
                 delaware.name: delaware,
                 florida.name: florida,
                 georgia.name: georgia,
                 hawaii.name: hawaii,
                 idaho.name: idaho,
                 illinois.name: illinois,
                 indiana.name: indiana,
                 iowa.name: iowa,
                 kansas.name: kansas,
                 kentucky.name: kentucky,
                 louisiana.name: louisiana,
                 maine.name: maine,
                 maryland.name: maryland,
                 massachusetts.name: massachusetts,
                 michigan.name: michigan,
                 minnesota.name: minnesota,
                 mississippi.name: mississippi,
                 missouri.name: missouri,
                 montana.name: montana,
                 nebraska.name: nebraska,
                 nevada.name: nevada,
                 new_hampshire.name: new_hampshire,
                 new_jersey.name: new_jersey,
                 new_mexico.name: new_mexico,
                 new_york.name: new_york,
                 north_carolina.name: north_carolina,
                 ohio.name: ohio,
                 oklahoma.name: oklahoma,
                 oregon.name: oregon,
                 pennsylvania.name: pennsylvania,
                 rhode_island.name: rhode_island,
                 south_carolina.name: south_carolina,
                 north_dakota.name: north_dakota,
                 south_dakota.name: south_dakota,
                 tennessee.name: tennessee,
                 texas.name: texas,
                 utah.name: utah,
                 vermont.name: vermont,
                 virginia.name: virginia,
                 washington.name: washington,
                 west_virginia.name: west_virginia,
                 wisconsin.name: wisconsin,
                 wyoming.name: wyoming}
    return state_dic


def display_cli_menu():
    """CLI menu to be displayed to user through the loop in main
    """
    print("1. Display all U.S. States in Alphabetical order along with the Capital, " +
          "State Population, and Flower.\n" +
          "2. Search for a specific state and display the appropriate Capital name, " +
          "State Population, and an image of the associated State Flower.\n" +
          "3. Provide a Bar graph of the top 5 populated States showing their overall " +
          "population.\n" +
          "4. Update the overall state population for a specific state.\n" +
          "5. Exit the program\n" +
          "------------------")


def selection_menu():
    """ Display CLI menu and check user input

    Returns:
        int: accepted user selection to
        decide which process to engage
    """
    while True:
        try:
            display_cli_menu()
            selection = int(input("> "))
            if 1 <= selection <= 5:
                break
            print("Not valid selection! Please pick between 1-5\n")
        except ValueError:
            print("Not a valid selection! Must be an int value!\n")
            continue

    return selection


def search_dictionary(dictionary):
    """Used by selections 2 and 4 to find a specific item from a dictionary

    Args:
        dictionary (State): the dictionary to be searched through,
        looking for a match in keys to the user's input

    Returns:
        State: returns a state object associated with the key matched
    """
    while True:
        print("\nEnter state you wish to search for:\n")
        search_term = input(">> ").title()
        returned_state = dictionary.get(search_term)
        if returned_state is None:
            print("Not a valid state or object does not exist!\n")
            continue
        break
    return returned_state


def __main__():
    """main program to run for lab3.py
    calls upon most other functions here in lab3.py
    """
    state_dictionary = initialize_state_dictionary()  # Load in state_dictionary to main

    print("Welcome to the Python State Capital and Flower List Application!\n------------------")
    while True:
        selection = selection_menu()

        if selection == 1:  # display all states in state_dictionary
            for key in state_dictionary:
                print(state_dictionary.get(key))

        elif selection == 2:  # Search for state by key, print info, render flower
            state = search_dictionary(state_dictionary)
            print(state)
            state.render_flower_img()

        elif selection == 3:  # Display top 5 populated states in bar graph
            state_object_list = []  # put all state objects into a list
            for key in state_dictionary:
                state_object_list.append(state_dictionary.get(key))

            top_5_list = sorted(state_object_list, reverse=True)[
                :5]  # get the top 5 from state_object_list

            state_names = []
            state_populations = []
            # append each top five to seperate lists according to name and population
            for state in top_5_list:
                state_names.append(state.name)
                state_populations.append(state.population)

            # build bargraph from names and populations
            plt.bar(state_names, state_populations)
            plt.show()

        elif selection == 4:  # Update overall state population
            # get specific state object
            state = search_dictionary(state_dictionary)
            print(f"\n{state.name} current population: {state.population:,}")
            # get / check new pop value
            while True:
                try:
                    new_pop = int(
                        input(f"\nEnter new population of {state.name} >> "))
                    if new_pop < 0:
                        print("\nPopulation cannot be less than 0!")
                        continue
                    break
                except ValueError:
                    print("Not a valid int value!")
                    continue
            # set the new population of the state in memory
            state.set_population(new_pop)
            print(
                f"New population of {state.name} has been set to: {state.population}\n")

        elif selection == 5:  # Exit program
            print("\nGoodbye!")
            return 0

        else:  # Exit program with error
            print("\nError! Not a valid selection! Exiting...")
            return 1


__main__()
