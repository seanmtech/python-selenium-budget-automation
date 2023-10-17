Python script that takes in a CSV file of transactions and levearges Selenium WebDriver to open a Chrome URL (the user's budget website, currently pointed at EveryDollar.com) and inputs all financial transactions from the CSV file into the budget site.

NOTES ON RUNNING PROGRAM:
    -- you MUST start from ZERO open Chrome instances for this to work currently

    -- for now, it's best to make sure you've logged in to Everydollar and then closed chrome
        -- before running the app (so it saves the state of your login for a while)

    -- be sure to manually update the 'csvData' string to point to your latest .csv file you want to parse
        -- make sure that file is saved in the same directory as the python program. 


-- FOR CHANGING EVERYDOLLAR'S MONTH
    -- manually update the hardcoded 'target_month' variable
    -- you may have to use Chrome devtools to inspect Everydollar's page to see what their specific month string is called
        -- e.g. "September" was actually "Sep" in their inline CSS code and "June" was "Jun" 


NOTES ON THE PROGRAM ITSELF
    -- it uses the Pandas library to read specific columns from a .csv file
# python-selenium-budget-automation


