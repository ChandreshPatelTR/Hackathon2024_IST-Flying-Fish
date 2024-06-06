import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
conn = snowflake.connector.connect(
    user='rachana.deepakchag@thomsonreuters.com',
    authenticator = 'externalbrowser',
    account='a206448_prod.us-east-1',
    role = 'A208192_GLOBALAIHACKATHON_DATAANALYTICS_MDS_READONLY',
    warehouse='A208192_GLOBALAIHACKATHON_DATAANALYTICS_MDS_WH',
    database='MYDATASPACE',
    schema='A208192_GLOBALAIHACKATHON_DATAANALYTICS'
)

cur = conn.cursor()
try:
    # Execute a query
    cur.execute("SELECT NUM_MINUTES,NUM_EVENTS FROM MYDATASPACE.A208192_GLOBALAIHACKATHON_DATAANALYTICS.FEATURE_EVENT LIMIT 10")
    rows = cur.fetchall()
    # Fetch the results
    NUMMINUTES = [row[0] for row in rows]
    NUMEVENTS = [row[1] for row in rows]
    print(NUMMINUTES)
    print(NUMEVENTS)
    plt.figure(figsize=(8, 8))
    plt.pie(NUMMINUTES, labels=NUMEVENTS, autopct='%1.1f%%', startangle=140)
    plt.title('LATITUDE LONGITUDE Pie Chart')
    plt.show()  
finally:
    # Close the cursor
    cur.close()