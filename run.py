from booking.booking import Booking

# inst  = Booking()
# inst.land_first_page()

with Booking(teardown=True) as bot:
    bot.land_first_page()
    # bot.change_currency('GBP')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date="2022-08-05",check_out_date="2022-08-17")
