import datetime

try:
    today = datetime.datetime.now()
    # fromtimestamp(0) method get the UNIX epoch as shown in the Instructions
    epoch = datetime.datetime.fromtimestamp(0)

    # formating dates with strftime from datetime lib
    formated_today = today.strftime("%b %-d %Y")
    formated_epoch = epoch.strftime("%B %-d, %Y")

    # delta between today an UNIX epoch
    delta = today - epoch
    # total_seconds method returns total seconds in the duration
    delta_in_seconds = delta.total_seconds()

    # formatting seconds to conform with instructions
    seconds_formated = f"{delta_in_seconds:,.4f}"
    scientific_notation = "{:.2e}".format(delta_in_seconds)
    # print results
    print(f"Seconds since {formated_epoch}: {seconds_formated} or \
          {scientific_notation} in scientific notation")
    print(formated_today)
except Exception as e:
    print(f"Error: {e}")
