"""
Code contributor:
Yueyue Wang: import, run_dashboard, run
Miao Li: run_clean
"""
import sys
from .dashboard import main_dash
from .scraping_data.pantry_scraper import food_pantry_tbl
from .scraping_data.yelp_simulation import yelp_simul
from .scraping_data.yelp_api import get_businesses, get_reviews
from .clean_func.gen_data import gen_data
from .clean_func.restaurants_cleanup import run_business_clean
from .clean_func.reviews_cleanup import run_clean_reviews


def run_dashboard():
    """
    Running dashboard
    Written by Yueyue
    """
    app = main_dash.app
    app.run_server(debug=False)

def run_pantry_scraper(): 
    """
    Running Pantry Scraper
    Written by: Maxine Xu
    """
    return food_pantry_tbl()

def run_api_simulation():
    """
    Running Yelp API Simulation
    Written by: Maxine Xu
    """
    return yelp_simul()

def run_yelp_reviews():
    """
    Gather reviews for Cook County restaurants
    Written by: Maxine Xu
    """
    get_businesses()
    return get_reviews()

def run_clean():
    """
    Clean datasets in the data directory
    Written by: Miao Li "gen_data()"; 
                Jariel Yang "run_business_clean() and run_clean_reviews()"
    """
    run_business_clean()
    run_clean_reviews()
    gen_data()

def run():
    """
    User type some arguments and we run a program
    """
    print("Welcome to Cook County Food Accessibility and Security App!")
    user_input = input(
        """Please Enter: 
                (1) For Dashboard, 
                (2) For Data Cleaning, 
                (3) For Scraping Data and API Interaction
                (4) Quit App.
                Option: """)
    if user_input == "1":
        print("running dashboard...")
        run_dashboard()
    elif user_input == "2":
        print("running data cleaning...")
        run_clean()
    elif user_input == "3":
        getdata_user_input = input(
            """Please Enter 
                (1) Scrape the list of emergency pantries from Cook County's Sheriff's Office,
                (2) Simulate interacting with Yelp's API,
                (3) Gather the full dataset of reviews for restaurants
                in Cook County using Yelp's API, or
                (4) Or anything else for quit program.
                Option: """)
        if getdata_user_input == "1":
            print("Scraping data...")
            print(run_pantry_scraper())
        elif getdata_user_input == "2":
            print("Starting Simulation...")
            run_api_simulation()
        elif getdata_user_input == "3":
            print("Getting reviews...")
            print("This process will likely take > 20 minutes") 
            print("If you would like to test interacting with the API, exit, rerun the function, and choose option (2) Simulate interacting with Yelp's API")
            run_yelp_reviews()
        else:
            sys.exit()

    else:
        sys.exit()

