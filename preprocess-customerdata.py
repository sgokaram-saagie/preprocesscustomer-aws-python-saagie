from pyathenajdbc import connect

conn = connect(s3_staging_dir='s3://saagiedemo-customer360/athena/',
               region_name='us-east-1')
try:
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM customer360.customer limit 10
        """)
        print(cursor.description)
        print(cursor.fetchall())
finally:
    conn.close()
