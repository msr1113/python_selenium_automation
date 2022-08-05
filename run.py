from booking.booking import Booking

# inst  = Booking()
# inst.land_first_page()

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.change_currency(currency='GBP')
